DOCKER_DIR = ./docker

# Docker files:
DOCKER_FILE = $(DOCKER_DIR)/Dockerfile
DOCKER_FILE_DEV = $(DOCKER_DIR)/Dockerfile.dev
DOCKER_FILE_DEV_GPU = $(DOCKER_DIR)/Dockerfile.dev.gpu

# Image names:
CONTAINER = sc2_datasets
DEVCONTAINER = sc2_datasets:devcontainer
DEVCONTAINER_GPU = sc2_datasets:devcontainer-gpu

# Test commands:
TEST_COMPOSE = $(DOCKER_DIR)/docker-test-compose.yml
TEST_COMMAND_RAW = poetry run pytest --ignore-glob='test_*.py' ./tests/test_cases/ --cov=sc2_datasets --cov-report term-missing --cov-report html --cov=xml 2>&1
TEST_COMMAND = "$(TEST_COMMAND_RAW)"
TEST_COMMAND_LOG = "$(TEST_COMMAND_RAW) | tee /app/logs/test_output.log"

##################################
######## Docker ##################
##################################
.PHONY: docker_build
docker_build: ## Build the Docker image.
	docker build \
		-f $(DOCKER_FILE) \
		-t $(CONTAINER) .

.PHONY: docker_build_dev
docker_build_dev: ## Build the development Docker image.
	docker build \
		-f $(DOCKER_FILE_DEV) \
		-t $(DEVCONTAINER) .

.PHONY: docker_build_dev_gpu
docker_build_dev_gpu: ## Build the development Docker image with GPU support.
	docker build \
		-f $(DOCKER_FILE_DEV_GPU) \
		-t $(DEVCONTAINER_GPU) .

##################################
######## GitHub Actions ##########
##################################
.PHONY: action_compose_build
action_compose_build:
	docker compose \
		-f $(TEST_COMPOSE) build

.PHONY: action_compose_test
action_compose_test: ## Triggered from a GitHub Action to run the tests for CI.
	docker compose -f $(TEST_COMPOSE) run \
		--rm --build sc2_datasets \
		sh -c $(TEST_COMMAND)

##################################
######## Documentation ###########
##################################
.PHONY: docs
docs: ## Generates the documentation.
	poetry run \
		make html \
		--directory docs/

.PHONY: help
help: ## Show available make targets
	@awk '/^[^\t ]*:.*?##/{sub(/:.*?##/, ""); printf "\033[36m%-30s\033[0m %s\n", $$1, substr($$0, index($$0,$$2))}' $(MAKEFILE_LIST)
