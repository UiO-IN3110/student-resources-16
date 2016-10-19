"""
The 'maybe'-operator

It is written '?' and indicate that the character is optional.
It is placed behind a character.
"""

import re

search_text = "One egg, many eggs, all the eggses."

regex = "eggs?"

search_results = re.findall(regex, search_text)
print(search_results)
