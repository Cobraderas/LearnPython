import re

# dir
print(dir(re))

my_dict = dict()
my_dict[1] = "1"
print(dir(my_dict))

# callable
print(callable(my_dict.keys))
print(callable(re.DOTALL))

# hasattr
print("hasattr")
print(hasattr(re, "items"))
print(hasattr(re, "match"))
print(hasattr(re, "IGNORECASE"))
print(hasattr(my_dict, "values"))

# getattr

print("getattr")
dict_keys = getattr(my_dict, "keys")
print(dict_keys)
print(dict_keys())

print(getattr(re, "DOTALL"))

# delattr  - deletes attributes , including functions (use with care or NOT at all)
print("dellattr")
# delattr(re, "compile")
regex = re.compile(".*", re.DOTALL)

# setattr
print("setattr")
re_compile = getattr(re, "compile")
delattr(re, "compile")
print(hasattr(re, "compile"))
setattr(re, "compile", re_compile)
print(hasattr(re, "compile"))

regex = re.compile("Ana.*", re.DOTALL)
if re.search(regex, "Ana are mere"):
    print("compile merge")

# dict
print("__dict__")
for k, v in dict.__dict__.items():
    print(str(k), " =", str(v))


class Test:
    what = "use this class for math stuff"

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def add(self, value):
        self.value += value

    @property
    def equals(self):
        return self.value

    @staticmethod
    def sum(value1, value2):
        return value1 + value2


test = Test(1)
print(test.equals)

for k, v in Test.__dict__.items():
    print(str(k), " =", str(v))


class DTest(Test):
    def __init__(self, value):
        Test.__init__(self, value)


print(Test.__subclasses__())
print(DTest.__bases__)

# globals
print("globals")
print(globals())  # gives information of what is loaded in your module


def functie():
    x = 1
    print(locals())


functie()


# global
int_var = 1


def modv1(value):
    int_var = value
    print(int_var)


modv1(3)
print(int_var)


def modv2(value):
    global int_var
    int_var += value


modv2(10)
print(int_var)

# nonlocal
