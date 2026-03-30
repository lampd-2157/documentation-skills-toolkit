.PHONY: serve lint link-check validate score build setup all check route wizard health-dashboard

## Development

serve:  ## Start MkDocs dev server (localhost:8000)
	cd demo-site && mkdocs serve

build:  ## Build demo site (strict mode)
	cd demo-site && mkdocs build --strict

## Quality

lint:  ## Run markdownlint on all .md files
	@npx markdownlint-cli2 "**/*.md" "#node_modules" "#demo-site" "#templates" --config config/.markdownlint.json || \
	(echo "" && \
	echo "=========================================" && \
	echo "How to fix lint errors:" && \
	echo "" && \
	echo "  AI Agent: paste the errors above into your AI agent and ask it to fix" && \
	echo "  Manual:   open file:line shown above, fix the issue, run 'make lint' again" && \
	echo "" && \
	echo "Common fixes:" && \
	echo "  MD022 — add blank line after heading" && \
	echo "  MD031 — add blank line around code fence" && \
	echo "  MD032 — add blank line around list" && \
	echo "  MD040 — add language to code fence (bash/text/yaml)" && \
	echo "=========================================" && \
	exit 1)

link-check:  ## Check internal/external links in docs
	find skills/ docs/ -name '*.md' | xargs npx markdown-link-check --config config/link-check.json --quiet

validate:  ## Validate skill files structure
	@python3 scripts/validate_skill.py || \
	(echo "" && \
	echo "=========================================" && \
	echo "How to fix validation errors:" && \
	echo "" && \
	echo "  AI Agent: paste the errors above into your AI agent and ask:" && \
	echo "            'fix this skill file to match the 6-section model'" && \
	echo "  Manual:   read skills/skill-template.md for required structure" && \
	echo "            6 sections: Context, Iron Law, Guardrails, Red Flags, Remember, Related Skills" && \
	echo "=========================================" && \
	exit 1)

spell:  ## Run spell check
	npx cspell "**/*.md"

score:  ## Score documentation quality
	python3 scripts/score_docs.py

security-scan:  ## Scan docs for hardcoded secrets
	bash scripts/docs-secret-scan.sh

## Setup

setup:  ## One-command setup (MkDocs + markdownlint + pre-commit)
	bash scripts/setup.sh

## Scaffold

new-runbook:  ## Create new runbook: make new-runbook TITLE="My Service"
	./scripts/docs-toolkit new runbook "$(TITLE)"

new-adr:  ## Create new ADR: make new-adr TITLE="Decision"
	./scripts/docs-toolkit new adr "$(TITLE)"

new-howto:  ## Create new how-to: make new-howto TITLE="Task"
	./scripts/docs-toolkit new howto "$(TITLE)"

new-training:  ## Create new training: make new-training TITLE="Topic"
	./scripts/docs-toolkit new training "$(TITLE)"

new-network:  ## Create new network topology: make new-network TITLE="Env"
	./scripts/docs-toolkit new network "$(TITLE)"

new-postmortem:  ## Create new postmortem: make new-postmortem TITLE="Incident"
	./scripts/docs-toolkit new postmortem "$(TITLE)"

new-maintenance:  ## Create new maintenance window: make new-maintenance TITLE="Task"
	./scripts/docs-toolkit new maintenance "$(TITLE)"

new-release-notes:  ## Create new release notes: make new-release-notes TITLE="vX.Y"
	./scripts/docs-toolkit new release-notes "$(TITLE)"

new-adr-madr:  ## Create new MADR ADR: make new-adr-madr TITLE="Decision"
	./scripts/docs-toolkit new adr-madr "$(TITLE)"

new-knowledge-check:  ## Create new knowledge check: make new-knowledge-check TITLE="Topic"
	./scripts/docs-toolkit new knowledge-check "$(TITLE)"

new-security-policy:  ## Create new security policy: make new-security-policy TITLE="Policy"
	./scripts/docs-toolkit new security-policy "$(TITLE)"

new-quick-reference:  ## Create new quick reference: make new-quick-reference TITLE="Tool"
	./scripts/docs-toolkit new quick-reference "$(TITLE)"

## Intelligence

route:  ## Analyze routing: make route DESC="viết API docs cho payment"
	./scripts/docs-toolkit route "$(DESC)"

wizard:  ## Interactive doc creation wizard
	./scripts/docs-toolkit wizard

health-dashboard:  ## Generate doc health dashboard
	python3 scripts/generate_health_dashboard.py

## Combined

all: lint validate build  ## Run lint + validate + build
check: lint link-check validate  ## Run all quality checks
