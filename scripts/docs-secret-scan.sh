#!/bin/bash
# ============================================================
# Documentation Secret Scanner
# Scans markdown files for hardcoded secrets and sensitive data
# Version: 4.1.0
# ============================================================
# Usage:
#   bash scripts/docs-secret-scan.sh                    # Scan all docs
#   bash scripts/docs-secret-scan.sh docs/my-file.md    # Scan specific file
# ============================================================

set -e

RED='\033[91m'
GREEN='\033[92m'
YELLOW='\033[93m'
BLUE='\033[94m'
BOLD='\033[1m'
NC='\033[0m'

# Files to scan
if [ -n "$1" ]; then
  FILES="$1"
else
  FILES=$(find docs/ skills/ prompts/ templates/ -name "*.md" 2>/dev/null)
  if [ -d "demo-site/docs" ]; then
    FILES="$FILES $(find demo-site/docs/ -name "*.md" 2>/dev/null)"
  fi
fi

if [ -z "$FILES" ]; then
  echo -e "${YELLOW}No files found to scan${NC}"
  exit 0
fi

TOTAL=0
ISSUES=0

echo -e "${BOLD}${BLUE}Documentation Secret Scanner${NC}"
echo "========================================="
echo ""

for file in $FILES; do
  [ ! -f "$file" ] && continue
  TOTAL=$((TOTAL + 1))
  FILE_ISSUES=0

  # Skip files allowed to use example IPs (demo, skills, prompts, security guide)
  IS_EXAMPLE=false
  if [[ "$file" == demo-site/* ]] || \
     [[ "$file" == skills/* ]] || \
     [[ "$file" == prompts/* ]] || \
     [[ "$file" == *security-placeholders* ]] || \
     [[ "$file" == *anti-patterns* ]]; then
    IS_EXAMPLE=true
  fi

  # 1. Private IPs (10.x, 172.16-31.x, 192.168.x) — skip example files
  if [ "$IS_EXAMPLE" = false ]; then
    MATCHES=$(grep -nP '(?<!\d)(10\.\d{1,3}\.\d{1,3}\.\d{1,3})(?!\d)' "$file" 2>/dev/null | grep -v "placeholder\|example\|PLACEHOLDER\|<.*IP.*>" || true)
    if [ -n "$MATCHES" ]; then
      echo -e "${RED}FOUND${NC} $file — Private IP (10.x.x.x):"
      echo "$MATCHES" | head -3
      FILE_ISSUES=$((FILE_ISSUES + 1))
    fi
  fi

  MATCHES=$(grep -nP '(?<!\d)(172\.(1[6-9]|2[0-9]|3[01])\.\d{1,3}\.\d{1,3})(?!\d)' "$file" 2>/dev/null || true)
  if [ -n "$MATCHES" ]; then
    echo -e "${RED}FOUND${NC} $file — Private IP (172.16-31.x):"
    echo "$MATCHES" | head -3
    FILE_ISSUES=$((FILE_ISSUES + 1))
  fi

  MATCHES=$(grep -nP '(?<!\d)(192\.168\.\d{1,3}\.\d{1,3})(?!\d)' "$file" 2>/dev/null || true)
  if [ -n "$MATCHES" ]; then
    echo -e "${RED}FOUND${NC} $file — Private IP (192.168.x):"
    echo "$MATCHES" | head -3
    FILE_ISSUES=$((FILE_ISSUES + 1))
  fi

  # 2. Password in connection strings (skip example files)
  if [ "$IS_EXAMPLE" = true ]; then
    MATCHES=""
  else
    MATCHES=$(grep -nP '://[^:]+:[^@\s]+@' "$file" 2>/dev/null | grep -v "placeholder\|example\|<.*>" || true)
  fi
  if [ -n "$MATCHES" ]; then
    echo -e "${RED}FOUND${NC} $file — Password in URL:"
    echo "$MATCHES" | head -3
    FILE_ISSUES=$((FILE_ISSUES + 1))
  fi

  # 3. API key patterns
  MATCHES=$(grep -nP '(sk-[a-zA-Z0-9]{20,}|AKIA[A-Z0-9]{16})' "$file" 2>/dev/null || true)
  if [ -n "$MATCHES" ]; then
    echo -e "${RED}FOUND${NC} $file — API key pattern:"
    echo "$MATCHES" | head -3
    FILE_ISSUES=$((FILE_ISSUES + 1))
  fi

  # 4. Slack webhooks
  MATCHES=$(grep -nP 'hooks\.slack\.com/services/' "$file" 2>/dev/null || true)
  if [ -n "$MATCHES" ]; then
    echo -e "${RED}FOUND${NC} $file — Slack webhook:"
    echo "$MATCHES" | head -3
    FILE_ISSUES=$((FILE_ISSUES + 1))
  fi

  # 5. Bearer tokens
  MATCHES=$(grep -nPi 'bearer [a-zA-Z0-9_\-]{20,}' "$file" 2>/dev/null | grep -v "placeholder\|example\|<.*>" || true)
  if [ -n "$MATCHES" ]; then
    echo -e "${RED}FOUND${NC} $file — Bearer token:"
    echo "$MATCHES" | head -3
    FILE_ISSUES=$((FILE_ISSUES + 1))
  fi

  ISSUES=$((ISSUES + FILE_ISSUES))
done

echo ""
echo "========================================="
echo -e "${BOLD}Scan Summary:${NC} $TOTAL file(s) scanned"
if [ "$ISSUES" -eq 0 ]; then
  echo -e "  ${GREEN}PASS — No secrets found${NC}"
else
  echo -e "  ${RED}FOUND $ISSUES potential secret(s)${NC}"
  echo ""
  echo -e "${BOLD}How to fix:${NC}"
  echo "  1. Replace real values with placeholders (see docs/security-placeholders.md)"
  echo "  2. Use <INTERNAL_IP>, <PASSWORD>, <API_TOKEN> etc."
  echo "  3. Use example.com for domains, 192.0.2.x for demo IPs"
  echo "  4. Run 'make security-scan' again to verify"
fi
echo "========================================="

exit 0
