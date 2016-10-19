"""
Character classes and quantifiers can be used together.
"""

import re

search_text = "One egg, many eggs, all the eggses."

regex = r"egg\w*"

search_results = re.findall(regex, search_text)
print(search_results)
