"""
Non-capturing groups is encurrage to separete grouping from capturing.
"""

import re

source_text = "mohahahahahahe"

regex_in = r"(\w*?)(?:ha)*(\w*?)"
regex_out = r"\2\1"

substituted_text = re.sub(regex_in, regex_out, source_text)
print(substituted_text)
