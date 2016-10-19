r"""
The any-key is represented with '.' (except the newline '\n').

The more you know.
"""

import re

search_text = "sing, sang, sung, song, seng."

regex = "s.ng"

search_results = re.findall(regex, search_text)
print(search_results)
