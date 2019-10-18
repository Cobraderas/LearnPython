import re

text = """re.search(pattern, string, flags=0)
Scan through string looking for the first location where the regular expression pattern produces a match, and return a 
corresponding match object. Return None if no position in the string matches the pattern; note that this is different 
from finding a zero-length match at some point in the string.
"""

# regex101.com


str1 = "[abc]"
if str1.startswith("[") and str1.endswith("]"):
    print(True)

match = re.search(r"^\[.*\]$", str1)
if match:
    print(True)


