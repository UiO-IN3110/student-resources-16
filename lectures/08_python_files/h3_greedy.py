"""
Once again with and without greedy operator.
"""

import re

search_text = "pineappleapplepineapple"

regex = r"\w*apple"
search_results = re.findall(regex, search_text)
print(search_results)

regex = r"\w*?apple"
search_results = re.findall(regex, search_text)
print(search_results)
