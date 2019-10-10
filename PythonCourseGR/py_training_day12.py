# os path glob and iglob

from glob import glob, iglob

# print(glob("*.txt"))  # returns a list with all txt files from current directory
# print(glob("p*.py"))
#
# print(glob("p[a-z][0-9][0-9].*"))
#
# # print(glob("c:\\windows\\*", recursive=True))
#
# for file in iglob("*.py", recursive=False):
#     print(file)
#

import os
# from os import path

print(os.path.abspath(__file__))

print(os.getcwd())

f_path = os.path.abspath(__file__)
print(os.path.basename(f_path))  # basename returns only the file name
print(os.path.dirname(f_path))
print(os.path.join(os.path.dirname(f_path), "test", "test1", "mate.py"))

f_path2 = os.path.join(f_path, "test", "test1", "mate.py")
# with open(f_path2) as f:
#     print(f.readline())

f_size = os.path.getsize(f_path)
print(f_size)

# with open(f_path) as f:
#     print(f.read(500))

print(os.path.isfile(f_path))
print(os.path.isfile(os.path.dirname(f_path)))

print(os.path.split(f_path))

print(os.path.splitext(f_path))
print(f_path.rsplit(".", 1))


