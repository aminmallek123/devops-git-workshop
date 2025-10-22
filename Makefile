.PHONY: venv install test clean

venv:
	python -m venv .venv && . .venv/bin/activate && pip install -U pip

install:
	pip install -r requirements.txt

test:
	pytest -q

clean:
	rm -rf __pycache__ .pytest_cache .venv