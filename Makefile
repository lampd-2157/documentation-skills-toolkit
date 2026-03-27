.PHONY: serve lint validate build setup all

## Development

serve:  ## Start MkDocs dev server (localhost:8000)
	cd demo-site && mkdocs serve

build:  ## Build demo site (strict mode)
	cd demo-site && mkdocs build --strict

## Quality

lint:  ## Run markdownlint on all .md files
	npx markdownlint-cli2 "**/*.md" "#node_modules" "#demo-site" "#templates" --config config/.markdownlint.json

validate:  ## Validate skill files structure
	python3 scripts/validate_skill.py

spell:  ## Run spell check
	npx cspell "**/*.md"

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

## Combined

all: lint validate build  ## Run lint + validate + build
