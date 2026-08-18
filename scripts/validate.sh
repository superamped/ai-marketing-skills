#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

for skill in skills/*/*; do
  skills-ref validate "$skill"
done

python3 scripts/validate_skills.py
