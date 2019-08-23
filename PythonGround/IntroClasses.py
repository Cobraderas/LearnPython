# create a Animal class
# class Animal(object):
#     def __init__(self, name):
#         self.name = name
#
#
# zebra = Animal("Jeff")
# print(zebra.name)

# ==============================================================

# Class definition
# class Animal(object):
#     """Makes cute animals."""
#     # For initializing our instance objects
#     def __init__(self, name, age, is_hungry):
#         self.name = name
#         self.age = age
#         self.is_hungry = is_hungry
#
# # Note that self is only used in the __init__()
# # function definition; we don't need to pass it
# # to our instance objects.
#
#
# zebra = Animal("Jeffrey", 2, True)
# giraffe = Animal("Bruce", 1, False)
# panda = Animal("Chad", 7, True)
#
# print(zebra.name, zebra.age, zebra.is_hungry)
# print(giraffe.name, giraffe.age, giraffe.is_hungry)
# print(panda.name, panda.age, panda.is_hungry)


# CLASS SCOPE
"""
each individual animal gets its own name and age
(since they’re all initialized individually),
but they all have access to the member variable is_alive,
since they’re all members of the Animal class
"""


class Animal(object):
    """Makes cute animals."""
    is_alive = True

    def __init__(self, name, age):
        self.name = name
        self.age = age


zebra = Animal("Jeffrey", 2)
giraffe = Animal("Bruce", 1)
panda = Animal("Chad", 7)

print(zebra.name, zebra.age, zebra.is_alive)
print(giraffe.name, giraffe.age, giraffe.is_alive)
print(panda.name, panda.age, panda.is_alive)

