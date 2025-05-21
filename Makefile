.PHONY: build-py
build-py:
	nuitka --module --remove-output --output-dir=compiled_py  fibonacci.py

.PHONY: build-rust
build-rust:
	maturin develop
