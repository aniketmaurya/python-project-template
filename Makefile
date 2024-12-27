build-docs:
	cp README.md docs/index.md

docsserve:
	uv run mkdocs serve

test:
	pytest

coverage:  ## Run tests with coverage
	coverage erase
	coverage run -m pytest
	coverage report -m
	coverage xml

clean:
	rm -rf dist
	find . -type f -name "*.DS_Store" -ls -delete
	find . | grep -E "(__pycache__|\.pyc|\.pyo)" | xargs rm -rf
	find . | grep -E ".pytest_cache" | xargs rm -rf
	find . | grep -E ".ipynb_checkpoints" | xargs rm -rf
	rm -f .coverage

style:
	isort --profile black .
	ruff format .

push:
	git push && git push --tags

build:
	python -m build

publish-test:
		$(style clean build)
		twine upload -r testpypi dist/*

publish-prod:
		$(style clean build)
		twine upload dist/*
