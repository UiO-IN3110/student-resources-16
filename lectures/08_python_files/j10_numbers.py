"""
Basic scientific notation.
"""
import re

regex = r"[\-+]?\d+\.\d*[Ee][+\-]\d+"

all_the_numbers = """
INTEGERS: 1 +2 -3
DECIMAL: +42.5 -.25 3.
SCIENCE: .23E+4 -4.00e-02 +1e1
CORNER_CASES: 1-2 4.- -E1- C++ .
"""

print(re.findall(regex, all_the_numbers))
