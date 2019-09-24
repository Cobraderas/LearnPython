# from collections import namedtuple
#
# data_dict = {}
# DataType = namedtuple("DataType", ["false", "true", "invalid"])
# dt = DataType(0, 1, -1)
#
#
# def save_data_type(lizt):
#     for item in lizt:
#         if type(item) == dt.false:
#             data_dict[str(item)] = dt.false
#         elif item == dt.true:
#             data_dict[str(item)] = dt.true
#         else:
#             data_dict[str(item)] = dt.invalid
#
#
# if __name__ == "__main__":
#     save_data_type([0, 1, 2, 4])
#     print(data_dict)


#  =====================================================================================================================


# class MyClass:  # prototypes a class to not crash
#     pass
#
#
# class MyClass2():
#     def __init__(self):
#         pass
#
#
# class MyClass3(object):
#     kind = "person"
#     def __init__(self, fname, lname):
#
#         self.first_name = fname
#         self.last_name = lname
#
#     def print(self):
#         print("I am a {}".format(self.kind))
#         # print("My name is: {} {}".format(self.last_name, self.first_name))
#         print("My name is: {} {}".format(self._format_text(self.last_name),
#                                          self.__format_text2(self.first_name)))
#
#     def _format_text(self, text):
#         return "*" + text
#
#     def __format_text2(self, text):
#         return text + "*"
#
#     def __str__(self):
#         return self.last_name
#
#     def __repr__(self):
#         return "MyClass3: {} {}".format(self.last_name, self.first_name)
#
#     def __bool__(self):
#         if not self.first_name and not self.last_name:
#             return False
#         else:
#             return True
#
#
# if __name__ == "__main__":
#
#     mc = MyClass()
#     mc.first_name = "George"
#     mc.last_name = "Radu"
#
#     print(mc.first_name)
#
#     MC2 = MyClass2()
#     mc3 = MyClass3("George", "Radu")
#     mc3.print()
#     mc3.first_name = "Ion"
#     mc3.print()
#     print(mc3._format_text("gigel"))
#     # print(mc3.__format_text2("gigel"))
#     print(mc3._MyClass3__format_text2("gigel"))  # access a class that was set supposedly private
#
#     print(str(3))
#     print(str(mc3))
#     print(mc3)
#     print(repr(mc3))
#     if mc3:
#         mc3.print()
#     mc3.last_name = ""
#     mc3.first_name = ""
#     if mc3:
#         mc3.print()


#  =====================================================================================================================


class MyClass:  # prototypes a class to not crash
    pass


a = 1
b = "abc"
if a is b:
    print(True)
else:
    print(False)

list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1
list3.append(4)
# if list1 is list2:
if list1 is list3:
    print(True)
else:
    print(False)

print(id(list1))
print(id(list2))
print(id(list3))

print(type(1))
mc = MyClass()
print(type(mc))


b = "mere"
c = "mere"

if b is c:
    print(True)

c = "".join(["m", "e", "r", "e"])
if b is c:
    print(True)
else:
    print(False)


print(isinstance(mc, MyClass))
mlist1 = [1, 2, "3", 4, "5"]
print([i if isinstance(i, int) else int(i) for i in mlist1])




