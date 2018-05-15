.PHONY: all

all: pytest flake8

pytest: .venv
	. .venv/bin/activate && pytest

flake8: .venv
	. .venv/bin/activate && flake8 ragnar

.venv:
	virtualenv-3 .venv
	. .venv/bin/activate && pip3 install -r requirements-test.pip
	. .venv/bin/activate && pip3 install -e .
