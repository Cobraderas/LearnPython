import re

text = """re.search(pattern, string, flags=0 [a-Z])
Scan through string looking for the first location where the regular expression pattern produces a match, and return a 
corresponding match object. Return None if no position in the string matches the pattern; note that this is different 
from finding a zero-length match at some point in the string.
"""

# regex101.com

# q|e means that will search for q or e

str1 = "[abc]"
if str1.startswith("[") and str1.endswith("]"):
    print(True)

match = re.search(r"^\[.*\]$", str1)
if match:
    print(True)


# regex = re.compile("^.*$", re.DOTALL | re.UNICODE | re.MULTILINE)
# regex = re.compile("^.*?(flags).*$", re.DOTALL | re.UNICODE | re.MULTILINE)
regex = re.compile("^.*?(f1(ag)s).*$", re.DOTALL | re.UNICODE | re.MULTILINE)

match = re.search(regex, text)
if match:
    print(match.group(0))
    print(match.group(1))
    print(match.group(2))

text2 = "wd 1gb"
x = re.search(r"(\w* )(\d)(gb)", text2)
y = {}
y[x.group(1)] = int(x.group(2))
print(y)

print(re.search("reg", text))
print(re.match("reg", text))
print(re.match("re\.", text))

print(re.fullmatch(".*", text, re.DOTALL))

match = re.fullmatch(".*?(flags).*", text, re.DOTALL)
if match:
    print(match.group(1))

sp_text = re.split("\(.*?\)", text)
for item in sp_text:
    print(item)

match = re.findall("str.*? ", text)
print(match)


match = re.finditer(".t.*?", text)
for item in match:
    print(item.group(0))

sub_text = re.sub("\d", "!", text)  # substitution wil take the string as an object and return the
                                    # string as a second object with the modifications done
print(sub_text)

sub_text = re.sub(" ", "_", text, 2)  # will make first 2 substitutions
print(sub_text)

esc_text = re.escape(text)
print(esc_text)

if re.match(esc_text, text):
    print("YUPII!")

re.DOTALL
re.MULTILINE
re.ASCII
re.UNICODE
re.IGNORECASE
