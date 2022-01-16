path := .

.PHONY: lint
lint: black isort flake	## Apply all the linters.


.PHONY: lint-check
lint-check:  ## Check whether the codebase satisfies the linter rules.
	@echo
	@echo "Checking linter rules..."
	@echo "========================"
	@echo
	@make lint-check


.PHONY: black
black: ## Apply black.
	@echo
	@echo "Applying black..."
	@echo "================="
	@echo
	@black --fast $(path)
	@echo


.PHONY: isort
isort: ## Apply isort.
	@echo "Applying isort..."
	@echo "================="
	@echo
	@isort $(path)


.PHONY: flake
flake: ## Apply flake8.
	@echo
	@echo "Applying flake8..."
	@echo "================="
	@echo
	@flake8 $(path)


.PHONY: help
help: ## Show this help message.
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'


.PHONY: test
test: ## Run the tests against the current version of Python.
	@cd django-polls && python manage.py test


.PHONY: migrate
migrate: ## Run the tests against the current version of Python.
	@cd django-polls \
    && python manage.py makemigrations \
	&& python manage.py migrate


.PHONY: dep-lock
dep-lock: ## Freeze deps in 'requirements.txt' file.
	@pip-compile requirements-dev.in -o requirements-dev.txt


.PHONY: dep-sync
dep-sync: ## Sync venv installation with 'requirements.txt' file.
	@pip-sync


.PHONY: install
install: ## Install all the dev dependencies and the app locally.
	@pip install -e .[dev_deps]


.PHONY: build
build: ## Build the app.
	@rm -rf dist
	@python -m build


.PHONY: upload
upload: build ## Build and upload to PYPI.
	@twine upload dist/*
