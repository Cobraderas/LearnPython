mstr1 = " \t ana are mere "
print(mstr1.strip())

mstr1 = " \t ana are mere "
print(mstr1.strip("\t"))

print(mstr1.lstrip("\t"))
print(mstr1.rstrip("\t"))


mstr2 = "gigi are pere"
print(mstr2.startswith("gigi"))
print(mstr2.startswith("gigi", 5))
print(mstr2.startswith("gigi", 0, 2))

print(mstr2.endswith("pere"))
print(mstr2.endswith("pere", 10))

# find index else -1

print(mstr2.find("are"))
print(mstr2.find("are", 7))

# if "are" in mstr2:
#     print(True)


pass1 = "!QWE123asd"
result = [False] * 5
for item in pass1:
    if item.isalpha():  # check letter
        result[0] = True
    if item.isdigit():
        result[1] = True
    if item.isupper():
        result[2] = True
    if item.islower():
        result[3] = True
        # printable = special chars, letters, numbers and spaces
    if item.isprintable() and not item.isspace() and not item.isalnum():
        result[4] = True

print(all(result))  # remove ! from pass1 to get a false


# ======================================================================================================================


import string

print(string.ascii_letters)
print(string.ascii_uppercase)
print(string.ascii_lowercase)
print(string.punctuation)
print(string.whitespace)
print(string.digits)


mstr3 = "abcd"
mstr4 = "ABCD"

print(mstr3.upper())
print(mstr4.lower())

mstr5 = " ".join(map(str, [1, 2,3]))
print(mstr5)

fpath = r"/home/george/bash.rc"
print(fpath.split("/"))
print(fpath.split("/")[-1])


print(fpath.split("/", 2))
print(fpath.rsplit("/", 1))
print(fpath.rsplit("/", 1)[-1])

mstr6 = """
abc
zxc
"""
print(mstr6.splitlines())

print("=" * 100)
print([False] * 10)

mlist1 = [i for i in range(100)]
print(mlist1)

mlist2 = [i for i in mlist1 if i % 2 == 0]
print(mlist2)

mlist3 = [(i, j) for i in range(5) for j in range(3)]
print(mlist3)

mlist4 = [i if i % 2 == 1 else 0 for i in mlist1]
print(mlist4)

mset1 = (i for i in "Ana aRe Mere" if i not in string.ascii_uppercase)
print(mset1)

list5 = [i for i in "Ana aRe Mere" if i not in string.ascii_uppercase]
print(list5)


mdict1 = {key: value for key, value in enumerate(string.ascii_uppercase)}
print(mdict1)
print(mdict1[5])

mdict2 = {key: value for key, value in zip([1, 2, 3, 4, 5], ["a", "b", "c", "d", "e", "f"])}
print(mdict2)
print(mdict2[2])

mdict3 = {key + 27: value for key, value in enumerate(string.ascii_lowercase)}
print(mdict3)

mdict4 = {**mdict1, **mdict3}
print(mdict4)


from collections import namedtuple

User = namedtuple("User", ["name", "type", "access"])
user = User("andrei", "admin", "0")
print(user.name)
print(user.type)
print(user.access)


