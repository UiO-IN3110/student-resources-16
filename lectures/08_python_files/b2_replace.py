"""
But it isn't hard to make an example that causes problems.
"""

source_text = """
The target word is apple.

But to make it hard, I will throw in a pineapple.
"""

substituted_text = source_text.replace("apple", "orange")

print(substituted_text)
