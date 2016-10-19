"""
Bringing grouping, extraction and alternatives together!
"""

import re

regex_in = r"((pre|post)\2?)fix"
regex_out = r"\1break"

source_text = "prefix, preprefix, postpostfix, quickfix, fix"

substituted_text = re.sub(regex_in, regex_out, source_text)
print(substituted_text)
