# regextester

Utility for testing SublimeLinter linter.py regexes

## Setup

Collect input for the test.  Run the linter on a lint target, and pipe the output to `file.txt`.

For example, `checkmake Makefile > file.txt`

## Usage

Write your regex changes in `test.py`.

Then run `make test` to test the regex.

Repeat as needed.
