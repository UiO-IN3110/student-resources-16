"""
Multiple callbacks in the same substitution.
"""

import re

regex_in = r"(funny)(bunny)"
regex_out = r"\2 \1"

source_text = "Hello funnybunny!"

substituted_text = re.sub(regex_in, regex_out, source_text)
print(substituted_text)
