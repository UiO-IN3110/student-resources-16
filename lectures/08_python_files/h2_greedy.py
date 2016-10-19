"""
Non-greedy modifiers.

All quantifiers are greedy; They grab as much as they can.
To make a quantifier non-greedy, add a '?' after it.

------ ----------
Greedy Non-greedy
------ ----------
+      +?
*      *?
?      ??
[a-z]  [a-z]?
------ ----------

Note the difference between the "maybe"-operator '?' and the non-greedy
modifier '?' is the character it follows.
"""
