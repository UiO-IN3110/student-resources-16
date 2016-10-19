"""
In substitutions, groups are for extraction.

Captured groups are refered backwards through numbering.
"""

import re

regex_in = r"(\w*)fix"
regex_out = r"\1break"

source_text = "prefix, infix, postfix, quickfix, fix"

substituted_text = re.sub(regex_in, regex_out, source_text)
print(substituted_text)
