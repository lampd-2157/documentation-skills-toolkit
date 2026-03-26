#!/bin/bash
# ============================================================
# Documentation Skills Toolkit — One-Command Setup
# Author: DulapReal (https://github.com/lampd-2157)
# License: MIT
# ============================================================
# Usage:
#   chmod +x setup.sh && ./setup.sh
#
# Hoặc từ toolkit root:
#   bash skills/templates/references/setup.sh
# ============================================================

set -e

echo "📝 Documentation Skills Toolkit — Setup"
echo "========================================="
echo ""

# ── Step 1: Python dependencies ────────────────────────────
echo "📦 Installing MkDocs + plugins..."
if [ -f "requirements.txt" ]; then
  pip install -r requirements.txt
elif [ -f "references/requirements.txt" ]; then
  pip install -r references/requirements.txt
else
  pip install mkdocs-material mkdocs-mermaid2-plugin \
    mkdocs-awesome-pages-plugin mkdocs-git-revision-date-localized-plugin \
    mkdocs-minify-plugin mkdocs-glightbox
fi
echo "  ✅ MkDocs installed"

# ── Step 2: Node dependencies ──────────────────────────────
echo ""
echo "📦 Installing markdownlint-cli2..."
if command -v npm &> /dev/null; then
  npm install -g markdownlint-cli2
  echo "  ✅ markdownlint-cli2 installed"
else
  echo "  ⚠️  npm not found — skip markdownlint. Install Node.js first."
fi

# ── Step 3: Pre-commit hooks ──────────────────────────────
echo ""
echo "🔗 Setting up pre-commit hooks..."
if command -v pre-commit &> /dev/null || pip install pre-commit; then
  if [ -f ".pre-commit-config.yaml" ]; then
    pre-commit install
    echo "  ✅ Pre-commit hooks installed"
  elif [ -f "references/pre-commit-config.yaml" ]; then
    cp references/pre-commit-config.yaml .pre-commit-config.yaml
    pre-commit install
    echo "  ✅ Pre-commit hooks installed (copied config)"
  else
    echo "  ⚠️  No pre-commit config found — skip"
  fi
fi

# ── Step 4: VS Code snippets ─────────────────────────────
echo ""
echo "📝 Setting up VS Code snippets..."
SNIPPETS_SRC=""
if [ -f "references/docs.code-snippets" ]; then
  SNIPPETS_SRC="references/docs.code-snippets"
elif [ -f "docs.code-snippets" ]; then
  SNIPPETS_SRC="docs.code-snippets"
fi

if [ -n "$SNIPPETS_SRC" ]; then
  mkdir -p .vscode
  cp "$SNIPPETS_SRC" .vscode/docs.code-snippets
  echo "  ✅ VS Code snippets installed (.vscode/docs.code-snippets)"
else
  echo "  ⚠️  Snippets file not found — skip"
fi

# ── Step 5: Markdownlint config ───────────────────────────
echo ""
echo "📋 Setting up markdownlint config..."
if [ ! -f ".markdownlint.json" ]; then
  if [ -f "references/markdownlint-config.json" ]; then
    cp references/markdownlint-config.json .markdownlint.json
    echo "  ✅ .markdownlint.json created"
  fi
else
  echo "  ✅ .markdownlint.json already exists"
fi

# ── Done ──────────────────────────────────────────────────
echo ""
echo "========================================="
echo "✅ Setup complete!"
echo ""
echo "Next steps:"
echo "  1. mkdocs serve          → Preview docs at http://localhost:8000"
echo "  2. mkdocs build --strict → Build for production"
echo "  3. Type 'doc-' in VS Code → Use documentation snippets"
echo "========================================="
