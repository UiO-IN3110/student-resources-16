"""
Multiple extractions at the same time!
"""

import re

regex = r"(\w*)fix(\w*)"

search_text = "prefix, fixpost"

search_results = re.findall(regex, search_text)
print(search_results)
