"""
Another solution with regular expression.
Brace yourself, this is going to be messy.
"""

import re

more_complex_logging_file = """
ERROR 1.1.1950 10:15 some_module.some_function: Try not to expect the word
ERROR at the beginning of the line.
ERROR 1.1.1950 11:47 some_module.some_function: Log lines can go across
multiple lines."""

search_string = r"^(ERROR [0-9.]+ [0-9:]+ \w+\.\w+: )"
simplified_logging_file = re.sub(
    search_string, r"@\1", more_complex_logging_file, flags=re.M)

for line in simplified_logging_file.split("@"):
    if line: print(line)
