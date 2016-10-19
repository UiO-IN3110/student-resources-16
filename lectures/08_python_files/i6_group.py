"""
Groups can be used to create multi character alternatives.
"""

import re

search_text = "One egg, many spams, all the hamses."

regex = r"(?:egg|spam|ham)\w*"

search_results = re.findall(regex, search_text)
print(search_results)
