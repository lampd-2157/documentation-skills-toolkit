#!/bin/bash
# ============================================================
# Documentation Skills Toolkit — One-Command Setup
# Author: DulapReal (https://github.com/lampd-2157)
# License: MIT
# Version: 3.1.0
# ============================================================
# Usage:
#   chmod +x setup.sh && ./setup.sh
#
# Hoặc từ toolkit root:
#   bash scripts/setup.sh
# ============================================================

set -e

echo "Documentation Skills Toolkit — Setup"
echo "========================================="
echo ""

# ── OS Detection ─────────────────────────────────────────
OS="unknown"
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
  if grep -qEi "(Microsoft|WSL)" /proc/version 2>/dev/null; then
    OS="wsl"
  else
    OS="linux"
  fi
elif [[ "$OSTYPE" == "darwin"* ]]; then
  OS="macos"
elif [[ "$OSTYPE" == "msys" || "$OSTYPE" == "cygwin" ]]; then
  OS="windows"
fi
echo "  Detected OS: $OS"
echo ""

# ── pip detection ────────────────────────────────────────
PIP_CMD="pip"
if ! command -v pip &> /dev/null; then
  if command -v pip3 &> /dev/null; then
    PIP_CMD="pip3"
    echo "  Using pip3 (pip not found)"
  else
    echo "  pip not found. Install Python first:"
    if [ "$OS" = "macos" ]; then
      echo "    brew install python3"
    elif [ "$OS" = "wsl" ] || [ "$OS" = "linux" ]; then
      echo "    sudo apt update && sudo apt install python3 python3-pip"
    fi
    exit 1
  fi
fi

# ── Step 1: Python dependencies ────────────────────────────
echo "Installing MkDocs + plugins..."
if [ -f "requirements.txt" ]; then
  $PIP_CMD install -r requirements.txt
elif [ -f "config/requirements.txt" ]; then
  $PIP_CMD install -r config/requirements.txt
else
  $PIP_CMD install mkdocs-material \
    mkdocs-awesome-pages-plugin mkdocs-git-revision-date-localized-plugin \
    mkdocs-minify-plugin mkdocs-glightbox
fi
echo "  MkDocs installed"

# ── Step 2: Node dependencies ──────────────────────────────
echo ""
echo "Installing markdownlint-cli2..."
if command -v npm &> /dev/null; then
  npm install -g markdownlint-cli2
  echo "  markdownlint-cli2 installed"
else
  echo "  npm not found — skip markdownlint."
  if [ "$OS" = "wsl" ]; then
    echo "  WSL tip: Install Node.js via nvm or 'sudo apt install nodejs npm'"
  elif [ "$OS" = "macos" ]; then
    echo "  Tip: brew install node"
  else
    echo "  Tip: Install Node.js first — https://nodejs.org/"
  fi
fi

# ── Step 3: Pre-commit hooks ──────────────────────────────
echo ""
echo "Setting up pre-commit hooks..."
if command -v pre-commit &> /dev/null || $PIP_CMD install pre-commit; then
  if [ -f ".pre-commit-config.yaml" ]; then
    pre-commit install
    echo "  Pre-commit hooks installed"
  elif [ -f "config/pre-commit.yaml" ]; then
    cp config/pre-commit.yaml .pre-commit-config.yaml
    pre-commit install
    echo "  Pre-commit hooks installed (copied config)"
  else
    echo "  No pre-commit config found — skip"
  fi
fi

# ── Step 4: VS Code snippets ─────────────────────────────
echo ""
echo "Setting up VS Code snippets..."
SNIPPETS_SRC=""
if [ -f "examples/docs.code-snippets" ]; then
  SNIPPETS_SRC="examples/docs.code-snippets"
elif [ -f "docs.code-snippets" ]; then
  SNIPPETS_SRC="docs.code-snippets"
fi

if [ -n "$SNIPPETS_SRC" ]; then
  mkdir -p .vscode
  cp "$SNIPPETS_SRC" .vscode/docs.code-snippets
  echo "  VS Code snippets installed (.vscode/docs.code-snippets)"

  # WSL: also copy to Windows VS Code if accessible
  if [ "$OS" = "wsl" ] && [ -d "/mnt/c/Users" ]; then
    WIN_USER=$(cmd.exe /c "echo %USERNAME%" 2>/dev/null | tr -d '\r' || true)
    if [ -n "$WIN_USER" ] && [ -d "/mnt/c/Users/$WIN_USER" ]; then
      WIN_VSCODE="/mnt/c/Users/$WIN_USER/.config/Code/User/snippets"
      if [ -d "$WIN_VSCODE" ] || mkdir -p "$WIN_VSCODE" 2>/dev/null; then
        cp "$SNIPPETS_SRC" "$WIN_VSCODE/docs.code-snippets" 2>/dev/null && \
          echo "  Also installed to Windows VS Code snippets"
      fi
    fi
  fi
else
  echo "  Snippets file not found — skip"
fi

# ── Step 5: Markdownlint config ───────────────────────────
echo ""
echo "Setting up markdownlint config..."
if [ ! -f ".markdownlint.json" ]; then
  if [ -f "config/.markdownlint.json" ]; then
    cp config/.markdownlint.json .markdownlint.json
    echo "  .markdownlint.json created"
  fi
else
  echo "  .markdownlint.json already exists"
fi

# ── Step 6: cspell config ────────────────────────────────
echo ""
echo "Setting up spell check config..."
if [ ! -f ".cspell.json" ]; then
  if [ -f "config/cspell.json" ]; then
    cp config/cspell.json .cspell.json
    echo "  .cspell.json created"
  fi
else
  echo "  .cspell.json already exists"
fi

# ── Step 7: Markdown link check config ───────────────────
echo ""
echo "Setting up link check config..."
if [ ! -f ".markdown-link-check.json" ]; then
  if [ -f "config/link-check.json" ]; then
    cp config/link-check.json .markdown-link-check.json
    echo "  .markdown-link-check.json created"
  fi
else
  echo "  .markdown-link-check.json already exists"
fi

# ── Step 8: Post-install validation ──────────────────────
echo ""
echo "Verifying installations..."

VERIFY_PASS=0
VERIFY_FAIL=0

if python3 -c "import mkdocs" 2>/dev/null; then
  MKDOCS_VER=$(python3 -c "import mkdocs; print(mkdocs.__version__)")
  echo "  ✅ MkDocs: $MKDOCS_VER"
  VERIFY_PASS=$((VERIFY_PASS + 1))
else
  echo "  ❌ MkDocs: not found"
  VERIFY_FAIL=$((VERIFY_FAIL + 1))
fi

if command -v npx &>/dev/null && npx markdownlint-cli2 --help &>/dev/null 2>&1; then
  echo "  ✅ markdownlint-cli2: available"
  VERIFY_PASS=$((VERIFY_PASS + 1))
else
  echo "  ⚠️  markdownlint-cli2: not found (optional)"
fi

if command -v pre-commit &>/dev/null; then
  echo "  ✅ pre-commit: $(pre-commit --version 2>&1 | head -1)"
  VERIFY_PASS=$((VERIFY_PASS + 1))
else
  echo "  ⚠️  pre-commit: not found (optional)"
fi

echo ""
echo "  Verified: $VERIFY_PASS passed, $VERIFY_FAIL failed"

# ── Done ──────────────────────────────────────────────────
echo ""
echo "========================================="
echo "Setup complete!"
echo ""
echo "Next steps:"
echo "  1. mkdocs serve              Preview docs at http://localhost:8000"
echo "  2. mkdocs build --strict     Build for production"
echo "  3. Type 'doc-' in VS Code    Use documentation snippets"
echo "  4. ./scripts/docs-toolkit    Scaffold new docs from templates"
echo "========================================="
