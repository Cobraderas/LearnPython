# # tuples
# # they are imutable
#
# x = [1, 2, 3]
# for i, item in enumerate(x):
#     print("{}  {}".format(i, item))
#
# t1 = ()
# t2 = tuple()
#
# t3 = tuple(x)
# print(t3)
# print(type(t3))
#
# t4 = (1, 2, 3)
# print(t4)
#
# t5 = 0, 1, 2, 3
# print(t5)
#
# t6 = 0,  # declares a tuple when you have only one value in it
# print(t6)
#
# t7 = 1, "a"  # can also be not homogenous
# print(t7)
# print(t7[0])
#
#
# i1 = 2
# i2 = 3
# i1, i2 = i2, i1
# print(i1)
# print(i2)
#
#
# # ===========================================================================================================
#
# # zip
#
# l1 = [1, 2, 3]
# l2 = ["a", "b", "c"]
#
# z1 = zip(l1, l2)
# for item in z1:
#     print(item)
#
# z1 = zip(l1, l2, (5, 6, 7))
# for item in z1:
#     print(item)
#
# # zip
#
# l3 = [(1, 3), (2, 4), (5, 6)]
# l11, l12 = zip(*l3)
#
# print(111)
# print(112)

# ===========================================================================================================

# # deque
# from collections import deque
#
# d1 = deque()
# d1.append(1)
# d1.append(2)
# d1.append(3)
#
# print(d1)
# x = d1.pop()
# print(d1)
#
# d1.appendleft(0)
# print(d1)
# d1.popleft()
# print(d1)
#
# d2 = deque([1, 2, 3, 4, 5], 3)  # the length becomes fixed and the append will eliminate one item and add another
# print(d2)
# d2.append(6)
# print(d2)


# ===========================================================================================================

# while <expression>:
#       code block
# else:
#       code block

l1 = [0, 1, 2, 3, 4, 5]
i = 1

# while i in l1:
#     print("still here")
#     i += 1

# while i in l1:
#     print("still here")
#     i += 1
# else:
#     print(i)


# while True:
#     if i in l1:
#         print("still here")
#         i += 1
#     else:
#         break


# print(str(12) + str(3))
#
# l4 = [1, 3, 2, 5, 4, 7, 6, 9, 8]
# print(sorted(l4))
# print(sorted(l4, reverse=True))
#
# # reversed
# for i in reversed(l4):
#     print(i, end=" "); print("\n")  # example of how it will accept ; like in java or other languages


i = 0
for i in range(10):
    print("null" if i % 2 == 0 else i)



