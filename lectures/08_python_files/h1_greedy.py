"""
How greedy do you want your operators to be?
"""

import re

search_text = "pineappleapplepineapple"

regex = r"\w*apple"
search_results = re.findall(regex, search_text)
print(search_results)
