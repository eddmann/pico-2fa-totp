IMAGE = python:3.10.0-alpine3.14
DOCKER = docker run --rm -v $(PWD):/app -w /app

.PHONY: test
test:
	@$(DOCKER) $(IMAGE) python -m doctest -v totp/*
