# different methods of defining a dictionary
dict1 = []
dict2 = {}
dict3 = {1: "a", 2: 3, True: False, 1.0: "1.0"}
# print(dict3[1])
# print(dict3[2])
# print(dict3.get(2, None))
# print(dict3.get(4, None))
#
#
# dict3[2] = "s"
# print(dict3.get(2, None))
#
# dict3[4] = "patru"
# print(dict3.get(4, None))
#
# dict3.setdefault(5, "NA")
# print(dict3.get(5))


# print(dict3.items())
# print(dict3.keys())
#
# if 1 in dict3.keys():
#     print("Found")
#
# print(dict3.values())
#
# dict3.clear()
# print(dict3.values())


# sets have the elements unique cannot have duplicate elements
# sets can also be used with math operations
set1 = set()
set2 = {1, 2, 3, 4}
set4 = {}  # dictionar


set3 = {4, 6, "6"}
# print(set2.intersection(set3))
# print(set2)
# # print(set2.intersection_update(set3))
# # print(set2)
#
# print(set2.union(set3))
# set2.update(set3)
# print(set2)

# print(set2.difference(set3))
print(set2.symmetric_difference(set3))

print(set2.difference_update(set3))
print(set2)


list1 = [1, 2, 2, 3, 4, 5]
list2 = list(set(list1))  # removes the duplicates from a list (fast short tip)
print(list1)
print(list2)


range(0, 3, 2)  # initial value < final value, stride
len_list = len(list1)
# for i in range(0, len_list):
#     print(list1[i])
#
#
# for item in list1:
#     print(item, end=" ")
#
#
# for _ in range(0, 3):
#     print("step")


for i in range(0, 10):
    if i > 20:
        break
else:
    print("have fun")


dict1 = {1: "a", 2: "b", 3: "c"}

for key, value in dict1.items():
    print("{}: {}".format(key, value))

# for key in dict1.keys():
#     print("{}".format(key))
#
# for value in dict1.values():
#     print("{}".format(value))

index = 0
for i, item in enumerate(list1):
    print("i = {} item = {}, ".format(i, item), end=" ")
    index += 1

# day 2 lists sets dict's
# sets are imutables


