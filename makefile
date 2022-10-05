all: test

run:
	python3 decode.py message.wav

test:
	python3 -m doctest decode.py

clean:
	rm -rf __pycache__ .mypy_cache