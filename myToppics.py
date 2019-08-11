# iterate over a dict
#
# d = {
#   "Name": "Guido",
#   "Age": 56,
#   "BDFL": True
# }
#
# print(d.items())


# my_dict = {
#     "Channel": "Master",
#     "Place": 30,
#     "On": True
# }
#
# print(my_dict.items())
# print(my_dict.values())
# print(my_dict.keys())
# print(my_dict.keys(), my_dict.values())


# for number in range(5):
#     print(number)
#
# d = {
#     "name": "Eric",
#     "age": 26
# }
#
# for key in d:
#     print(key, d[key])
#
# for letter in "Eric":
#     print(letter)


# my_dict = {
#     "Channel": "Master",
#     "Place": 30,
#     "On": True
# }
#
# for i in my_dict:
#     print(i, my_dict[i])


# # list comprehension example:
# evens_to_50 = [i for i in range(51) if i % 2 == 0]
# print(evens_to_50)
#
# # create a new_list populated by the numbers one to five:
# new_list = [x for x in range(1, 6)]
# print(new_list)
#
# # create a new_list populated by the numbers one to five doubled:
# doubles = [x * 2 for x in range(1, 6)]
# print(doubles)
#
# # doubled numbers from above that are evenly divisible by three
# doubles_by_3 = [x * 2 for x in range(1, 6) if (x * 2) % 3 == 0]
# print(doubles_by_3)
#
#
# # ex line: doubles_by_3 = [x * 2 for x in range(1, 6) if (x * 2) % 3 == 0]
# # include the squares of the even numbers between 1 to 11 not including 0
# # x ** 2 squares a nr
# # x % 2 == 0 checks if is even
# even_squares = [x ** 2 for x in range(1, 12) if x % 2 == 0]
# print(even_squares)


# c = ['C' for x in range(5) if x < 3]
# print(c)
#
# cubes_by_four = [x ** 3 for x in range(1, 11) if (x ** 3) % 4 == 0]
# print(cubes_by_four)


# # list slicing [start:end:stride]
# l = [i ** 2 for i in range(1, 11)]  # Should be [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# print(l)
# print(l[2:9:2])  # slice the list; Should be [9, 25, 49, 81]
#
# # how stride work in list slicing:
# my_name = "BobbyTarantino"
#
# print(my_name[::1])  # BobbyTarantino
# print(my_name[::-1])  # onitnaraTybboB
#
# print(my_name[::2])  # Bbyaatn
# print(my_name[::-2])  # oinrTbo


# If you don’t pass a particular index to the list slice, Python will pick a default.
# The default starting index is 0.
# The default ending index is the end of the list.
# The default stride is 1.
#
# to_five = ['A', 'B', 'C', 'D', 'E']
#
# print(to_five[3:])
# # prints ['D', 'E']
#
# print(to_five[:2])
# # prints ['A', 'B']
#
# print(to_five[::2])
# # print ['A', 'C', 'E']


# my_list = list(range(1, 11))
# backwards = my_list[::-1]
# print(backwards)


# grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]
#
#
# def print_grades():  # why is the param needed when is not used?
#     for i in grades:
#         print(i)
#
#
# print_grades()


# # code adapted from py 2 example
# to_one_hundred = list(range(101))  # converts the iterator to list
#
# backwards_by_tens = to_one_hundred[::-10]
# print(backwards_by_tens)


# to_21 = list(range(1, 22))
# odds = to_21[::2]
# middle_third = to_21[7:14]
# print(to_21)
# print(odds)
# print(middle_third)

# threes_and_fives = [x for x in range(1, 16) if x % 3 == 0 or x % 5 == 0]
# print(threes_and_fives)


# garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"
# message = garbled[::-2]
# print(message)







