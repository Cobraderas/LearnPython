# f = open("TestRead.txt", "r")
# print(f.read())

# print(f.read(5))

# print(f.readline())

# for x in f:
#    print(x)

# o write to an existing file, you must add a parameter to the open() function:
# "a" - Append - will append to the end of the file
# "w" - Write - will overwrite any existing content

f = open("TestRead.txt", "a")
f.write("Now the file has one more line!")


# To create a new file in Python, use the open() method, with one of the following parameters:
# "x" - Create - will create a file, returns an error if the file exist
# "a" - Append - will create a file if the specified file does not exist
# "w" - Write - will create a file if the specified file does not exist




