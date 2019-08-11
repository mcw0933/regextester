FOO = echo "foo"

.DEFAULT: help
help:
	@echo "make test"
	@echo "   Run regex test"

test:
	@python test.py

.PHONY: all clean test help
