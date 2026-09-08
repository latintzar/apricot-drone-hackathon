.PHONY: replay test
replay:
	python3 replay.py
test:
	python3 -m unittest discover -s tests -v
