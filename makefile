
# Double hash comments are used to provide a description for each target
# @ is used to prevent the command from being printed to the console
# 'grep' is used to filter the targets and their descriptions
# 'awk' is used to format the output
# The 'printf' command is used to print the target and its description in a formatted way
# $$1 and $$2 are used to access the first and second fields of the output of the 'awk' command
# .PHONY is used to declare the targets that are not associated with files
# .DEFAULT_GOAL is used to set the default target to be executed

.PHONY: help venv activate install test up run down lint format


help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

venv: ## Create a virtual environment
	@echo "Creating virtual environment..."  ## python -m venv .venv

activate: ## Activate the virtual environment
	@echo "Activating virtual environment..."  ## source .venv/Scripts/activate.bat

install: ## Install dependencies
	@echo "Installing all dependencies..."  ## pip install -r requirements.txt

test: ## Run tests
	@echo "Running tests..."  ## python -m unittest discover tests

up: ## Start services
	@echo "Starting services as Docker..."  ## docker-compose -f compose.yaml up -d

run: ## Run the application
	@echo "Running app..."
	@flet run src/main.py

down: ## Stop services
	@echo "Stopping services as Docker..."  ## docker-compose -f compose.yaml down

lint: ## Lint the code
	@echo "Linting the code (with Ruff)..."  ## python -m ruff check

format: ## Format the code
	@echo "Formating the code (with Ruff)..."  ## python -m ruff format


.DEFAULT_GOAL := help