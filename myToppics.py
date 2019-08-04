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












