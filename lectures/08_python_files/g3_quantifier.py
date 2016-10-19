"""
For the words with variable length vowels.
"""

import re

search_text = "no, no, nooooooo."

regex = "no+"

search_results = re.findall(regex, search_text)

print(search_results)
