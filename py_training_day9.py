# DO NOT REMOVE THIS: FOLDER TREE WAS CREATED WRONG AND WILL WORK ONLY FROM ROOT

# def beauty(func):
#     def beauty_print(*args, **kwargs):
#         print("You have added")
#         func(*args, **kwargs)
#         print("HO! HO! HO!")
#     return beauty_print
#
#
# def beauty2(func):
#     def beauty_print(*args, **kwargs):
#         print("You have ADDED!")
#         func(*args, **kwargs)
#         print("HOBO! HO! HOBO!")
#     return beauty_print
#
#
# class Craciun:
#     @beauty
#     @beauty2
#     def add_lights(self, lights_no):
#         print("{} lights!".format(lights_no))
#
#
# def tag(tag_name):
#     def tag_decorator(func):
#         def func_wrapper(name):
#             return "<{0}>{1}</{0}>".format(tag_name, name)
#         return func_wrapper
#     return tag_decorator
#
#
# @tag("p")
# def tagged_text(text):
#     return text
#
#
# if __name__ == "__main__":
#     cr = Craciun()
#     cr.add_lights(50)
#
#     print(tagged_text("this is a paragraph"))


# ======================================================================================================================

# from collections import deque
# from collections import *  # avoid at all costs
# import re
# import re as r

# deq = deque()
# str = "ana are mere".split()
# re.split()  # the code is not compilable only serves as example
# r.split()  # the code is not compilable only serves as example

from test.mate_adv import MateAdv
from test import Mate
from test import *


if __name__ == "__main__":
    # mate = MateAdv()
    # print(mate.sum(1, 5))

    mate = Mate()
    print(mate.sum(1, 2))
    # matead = MateAdv
