DEPLOY_DIR = ./docker

TEST_COMPOSE = $(DEPLOY_DIR)/docker-test-compose.yml

action_compose_build:
	docker-compose -f $(TEST_COMPOSE) build

action_compose_test: ## Triggered from a GitHub Action to run the tests for CI.
	docker-compose -f $(TEST_COMPOSE) run --rm django sh -c "python manage.py test --pattern=*_test.py 2>&1"

.PHONY: help
help: ## Show available make targets
	@awk '/^[^\t ]*:.*?##/{sub(/:.*?##/, ""); printf "\033[36m%-30s\033[0m %s\n", $$1, substr($$0, index($$0,$$2))}' $(MAKEFILE_LIST)
