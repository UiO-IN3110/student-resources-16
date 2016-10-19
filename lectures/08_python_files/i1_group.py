"""
Group extraction.

For when you are not interested in everything in the regex string.
"""

import re

regex = "(\w*)fix"

search_text = "prefix, infix, postfix, quickfix, fix"

search_results = re.findall(regex, search_text)
print(search_results)
