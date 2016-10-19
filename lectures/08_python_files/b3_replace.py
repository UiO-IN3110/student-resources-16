"""
Solution using regular expresion.

(Don't worry if you don't understand the syntax yet.)
"""

import re

source_text = """
The target word is apple.

But to make it hard, I will throw in a pineapple.
"""

substituted_text = re.sub(r"\bapple\b", "orange", source_text)

print(substituted_text)
