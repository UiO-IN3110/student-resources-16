"""
Cavet: When is a newline an actual new line?

Flagging with `re.M`/`re.MULTILINE`.
"""

import re

search_text = """apples, oranges, and
pineapples."""

regex = r"^\w+"

search_results = re.findall(regex, search_text)
print(search_results)

search_results = re.findall(regex, search_text, flags=re.M)
print(search_results)
