"""
Making life really hard.
"""

more_complex_logging_file = """
ERROR 1.1.1950 10:15 some_module.some_function: Try not to expect the word
ERROR at the beginning of the line.
ERROR 1.1.1950 11:47 some_module.some_function: Log lines can go across
multiple lines."""

for line in more_complex_logging_file.split("\n"):
    if line.startswith("ERROR"):
        print(line)
