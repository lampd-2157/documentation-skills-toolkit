#!/usr/bin/env bash
# bump-version.sh — Update all version footers to match the given version
# Usage: bash scripts/bump-version.sh 5.4.0
#   or:  make bump-version V=5.4.0

set -euo pipefail

VERSION="${1:-}"
DATE=$(date +%Y-%m-%d)

if [[ -z "$VERSION" ]]; then
  echo "Usage: bash scripts/bump-version.sh <version>"
  echo "Example: bash scripts/bump-version.sh 5.4.0"
  exit 1
fi

# Validate semver format
if ! [[ "$VERSION" =~ ^[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
  echo "Error: Version must be semver format (e.g., 5.4.0)"
  exit 1
fi

echo "Bumping version to $VERSION ($DATE)..."

# Files with "> Version X.Y.Z | YYYY-MM-DD" or "> **Version:** X.Y.Z | **Updated:** YYYY-MM-DD"
FILES_FOOTER=(
  "README.md"
  "AGENTS.md"
  "CONTRIBUTING.md"
  "prompts/README.md"
  "prompts/interview-before-create.md"
)

for file in "${FILES_FOOTER[@]}"; do
  if [[ -f "$file" ]]; then
    # Pattern: > **Version:** X.Y.Z | **Updated:** YYYY-MM-DD
    sed -i -E "s/(> \*\*Version:\*\* )[0-9]+\.[0-9]+\.[0-9]+( \| \*\*Updated:\*\* )[0-9]{4}-[0-9]{2}-[0-9]{2}/\1${VERSION}\2${DATE}/" "$file"
    # Pattern: > Version X.Y.Z | YYYY-MM-DD
    sed -i -E "s/(> Version )[0-9]+\.[0-9]+\.[0-9]+( \| )[0-9]{4}-[0-9]{2}-[0-9]{2}/\1${VERSION}\2${DATE}/" "$file"
    echo "  Updated: $file"
  else
    echo "  Warning: $file not found, skipping"
  fi
done

# README badge
if [[ -f "README.md" ]]; then
  sed -i -E "s/version-[0-9]+\.[0-9]+\.[0-9]+-blue/version-${VERSION}-blue/" "README.md"
  echo "  Updated: README.md badge"
fi

# AGENT-CARDS.json
if [[ -f "skills/AGENT-CARDS.json" ]]; then
  sed -i -E "s/\"version\": \"[0-9]+\.[0-9]+\.[0-9]+\"/\"version\": \"${VERSION}\"/" "skills/AGENT-CARDS.json"
  echo "  Updated: skills/AGENT-CARDS.json"
fi

echo ""
echo "Done! Version bumped to $VERSION."
echo "Next steps:"
echo "  1. Update CHANGELOG.md with new version section"
echo "  2. Run 'make check-versions' to verify"
echo "  3. Commit: git commit -am 'chore: bump version to $VERSION'"
