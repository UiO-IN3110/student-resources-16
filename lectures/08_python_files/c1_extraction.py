"""
Another example: data extraction.
"""

your_day_of_mill_python_logging_file = """
INFO:  Write code for assignment in INF3331.
DEBUG: Too lazy to document code.
INFO:  Submit code on Github.
ERROR: Assignment fail.
DEBUG: Go home and cry.
"""

for line in your_day_of_mill_python_logging_file.split("\n"):
    if line.startswith("ERROR"):
        print(line)
