# file operations
# https://stackabuse.com/file-handling-in-python/


# using with that closes the file automatically
# with open("py_training_day6.py") as f:
#     buffer = f.read()
#     print(buffer)
# print(f.closed)  # check if the file is closed

# classic method to open and read file
# without using with
# f = open("py_training_day6.py")
# buffer = f.read()  # reads the whole file and returns and saves the content in variable
# print(buffer)
# f.close()


# f = open("py_training_day6.py")
# for line in f:
#     print(line)


# f = open("py_training_day6.py")
# print(f.readline())
# print(f.readline())
# print(f.readline())


# f = open("py_training_day6.py")
# lines = f.readlines()
# for line in lines:
#     print(line)

#
# f = open("testa.txt", "a")  # appends
# f.write("flu")


# f = open("testa.txt", "r+", buffering=0)  # buffering=0 for binary, buffering=1 text mode line buffering
# f.write("AZERTY")


# f = open("testa.txt")
# f.readline()
# print(f.tell())
# f.seek(0)
# f.readline()
# print(f.tell())
#
# f.seek(25)
# f.readline()
# print(f.tell())


f = open("testa.txt")
f.readline()
print(f.tell())
f.seek(0, 1)
print(f.read(5))
print(f.tell())

# seek(0)  # returns start of file
# seek(0, 2)  # returns end of file
