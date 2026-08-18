#!/usr/bin/env python3
"""Validate Agent Skills packages and repository wiring."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
MARKETPLACE = ROOT / ".claude-plugin" / "marketplace.json"
KEBAB = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
FRONTMATTER = re.compile(r"\A---\n(.*?)\n---(?:\n|\Z)", re.DOTALL)
MARKDOWN_LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
SECRET_PATTERNS = {
    "GitHub token": re.compile(r"\b(?:ghp|github_pat)_[A-Za-z0-9_]{30,}\b"),
    "OpenAI-style key": re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
    "unexpanded bearer token": re.compile(r"Bearer\s+(?!\$\{|<|\{\{)[A-Za-z0-9._~-]{24,}"),
}


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def skill_directories() -> list[Path]:
    return sorted(p.parent for p in SKILLS.glob("*/*/SKILL.md"))


def validate_skills(errors: list[str]) -> set[str]:
    relative_dirs: set[str] = set()
    for directory in skill_directories():
        skill_file = directory / "SKILL.md"
        relative = directory.relative_to(ROOT).as_posix()
        relative_dirs.add(f"./{relative}")
        text = skill_file.read_text(encoding="utf-8")
        match = FRONTMATTER.match(text)
        if not match:
            fail(errors, f"{skill_file.relative_to(ROOT)}: missing YAML frontmatter")
            continue
        try:
            metadata = yaml.safe_load(match.group(1))
        except yaml.YAMLError as exc:
            fail(errors, f"{skill_file.relative_to(ROOT)}: invalid YAML: {exc}")
            continue
        if not isinstance(metadata, dict):
            fail(errors, f"{skill_file.relative_to(ROOT)}: frontmatter must be a mapping")
            continue

        name = metadata.get("name")
        description = metadata.get("description")
        if name != directory.name:
            fail(errors, f"{skill_file.relative_to(ROOT)}: name {name!r} must match directory {directory.name!r}")
        if not isinstance(name, str) or not KEBAB.fullmatch(name):
            fail(errors, f"{skill_file.relative_to(ROOT)}: name must be kebab-case")
        if not isinstance(description, str) or not description.strip():
            fail(errors, f"{skill_file.relative_to(ROOT)}: description is required")
        elif len(description) > 1024:
            fail(errors, f"{skill_file.relative_to(ROOT)}: description exceeds 1024 characters")
        compatibility = metadata.get("compatibility")
        if not isinstance(compatibility, str) or not compatibility.strip():
            fail(errors, f"{skill_file.relative_to(ROOT)}: compatibility is required")
    return relative_dirs


def validate_marketplace(errors: list[str], actual_skills: set[str]) -> None:
    try:
        data = json.loads(MARKETPLACE.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(errors, f"{MARKETPLACE.relative_to(ROOT)}: invalid JSON: {exc}")
        return
    plugins = data.get("plugins") or []
    if len(plugins) != 1:
        fail(errors, ".claude-plugin/marketplace.json: expected exactly one plugin")
        return
    listed = set(plugins[0].get("skills") or [])
    missing = actual_skills - listed
    stale = listed - actual_skills
    if missing:
        fail(errors, f"marketplace missing skills: {', '.join(sorted(missing))}")
    if stale:
        fail(errors, f"marketplace lists missing directories: {', '.join(sorted(stale))}")


def validate_links(errors: list[str]) -> None:
    for markdown in sorted(ROOT.glob("*.md")):
        text = markdown.read_text(encoding="utf-8")
        for target in MARKDOWN_LINK.findall(text):
            target = target.strip().split("#", 1)[0].split("?", 1)[0]
            if not target or target.startswith(("http://", "https://", "mailto:")):
                continue
            candidate = (markdown.parent / target).resolve()
            try:
                candidate.relative_to(ROOT.resolve())
            except ValueError:
                fail(errors, f"{markdown.name}: link escapes repository: {target}")
                continue
            if not candidate.exists():
                fail(errors, f"{markdown.name}: broken local link: {target}")


def validate_likely_secrets(errors: list[str]) -> None:
    ignored_parts = {".git", "__pycache__"}
    for path in ROOT.rglob("*"):
        if not path.is_file() or any(part in ignored_parts for part in path.parts):
            continue
        if path.suffix.lower() in {".png", ".jpg", ".jpeg", ".gif", ".webp"}:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for label, pattern in SECRET_PATTERNS.items():
            if pattern.search(text):
                fail(errors, f"{path.relative_to(ROOT)}: possible {label}")


def main() -> int:
    errors: list[str] = []
    actual_skills = validate_skills(errors)
    validate_marketplace(errors, actual_skills)
    validate_links(errors)
    validate_likely_secrets(errors)

    if errors:
        print(f"Validation failed with {len(errors)} error(s):", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"Validated {len(actual_skills)} Agent Skills, marketplace registration, links, and secret patterns.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
