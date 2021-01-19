.PHONY: help clean dist release
.DEFAULT_GOAL := help

define PRINT_HELP_PYSCRIPT
import re, sys

matches = [re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line) for line in sys.stdin]
print(f"\nusage: make {'|'.join([m.group(1) for m in matches if m])}\n")
for match in matches:
	if match:
		target, help = match.groups()
		print("  %-10s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

help:
	@python3 -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

clean: ## to remove all temporary, test, and build artifacts.
	rm -rf .coverage*
	rm -rf .eggs/
	rm -rf .stestr/
	rm -rf .tox/
	rm -rf AUTHORS
	rm -rf ChangeLog
	rm -rf build/
	rm -rf cover/
	rm -rf dist/
	find . -name '__pycache__' -exec rm -rf {} +

release: dist ## to package and upload a release.
	find . -name '*.egg-info' -exec rm -rf {} +
	twine upload dist/*

dist: clean ## to build source and wheel packages.
	python3 setup.py sdist
	python3 setup.py bdist_wheel
	ls -l dist
