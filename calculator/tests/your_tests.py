#!/usr/bin/env python3
from calculator_adapter import run


### ADD AT LEAST TWO TESTS HERE!

assert run("0 * 0").output == "0"
assert run("5 * 1").output == "5"

###

print("All tests passed!")
