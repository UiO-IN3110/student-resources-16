"""
Let us start from scratch.

Letters and numbers are them self.
"""

import re

spam = "spam"
eggs = "eggs"

search_text = "spammy eggs and eggy spam."

substituted_text = re.sub(spam, eggs, search_text)
print(substituted_text)

search_results = re.findall(spam, search_text)
print(search_results)
