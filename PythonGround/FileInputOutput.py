# my_list = [i ** 2 for i in range(1, 11)]
# # Generates a list of squares of the numbers 1 - 10
#
# f = open("demofile.txt", "w")
#
# for item in my_list:
#     f.write(str(item) + "\n")
#
# f.close()


# pass "r+" as a second argument to the function so the file will allow you to read and write to it
# my_file = open("demofile.txt", "r+")


# my_list = [i ** 2 for i in range(1, 11)]
#
# my_file = open("demofile.txt", "a")  # "a" appends the text
#
# for item in my_list:
#     my_file.write(str(item) + "\n")
#
# my_file.close()


# read from file & print to console
# my_file = open("demofile.txt", "r")
# print(my_file.read())
# my_file.close()


# read from a file line by line, rather than pulling the entire file in at once
# my_file = open("TestRead.txt", "r")
#
# print(my_file.readline())
# print(my_file.readline())
# print(my_file.readline())
# print(my_file.readline())
#
# my_file.close()


# # Use a file handler to open a file for writing
# write_file = open("TestRead.txt", "w")
#
# # Open the file for reading
# read_file = open("TestRead.txt", "r")
#
# # Write to the file
# write_file.write("Not closing files is VERY BAD.")
# write_file.close()
#
#
# # Try to read from the file
# print(read_file.read())
# read_file.close()


# closing the file automaticaly with "with" and "as"
# with open("TestRead.txt", "w") as textfile:
#     textfile.write("Success!")


