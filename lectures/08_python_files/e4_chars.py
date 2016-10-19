"""
Do you have the time?

Note the 'r' prefixes here!
"""

import re

search_text = "The bar is open between 18:04 and 02:00 every friday."
regex = r"\d\d:\d\d"
search_results = re.findall(regex, search_text)
print(search_results)
