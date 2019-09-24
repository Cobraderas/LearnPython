# functions
def func1():
    print("initialise 4")


def func2(var1, var2):
    return var1 + var2


def func3():
    def ff3(v1):
        print(v1)
    ff3("string")


def factorial(n):
    return n * factorial(n - 1) if n > 1 else 1


l1 = [1, 2]


def ml1(list1):
    list1.append(3)


def ml2(list2=[]):
    list2.append(1)
    print(list2)


def func4(b, c=1, d=2):
    print(b)
    print(c)
    print(d)


def func5(*args):
    for arg in args:
        print(arg, end=" ")


# def func6(**kwargs):
#     for kw in kwargs:
#         print(kw, kwargs(kw))


def func7(*args, **kwargs):
    for arg in args:
        print(arg)
    for kw in kwargs:
        print(kw, kwargs)


def funct8(a, b):
    a += 1
    b += 1
    return a, b


def sort_help(item):
    return item[0]


if __name__ == "__main__":
    #
    # l2 = [("z", 3), ("x", 1), ("t", 2)]
    # print(sorted(l2, key=sort_help))
    # print(sorted(l2, key=lambda i: i[1]))

    l3 = ["1", "2", "3"]
    m1 = map(int, l3)
    print(type(m1))
    print(list(m1))

    # any()
    print(any([1, 2, False]))
    # all()
    print(all([True,  []]))

    # filter
    print(list(filter(lambda x: x % 2, [i for i in range(10)])))


    #
    # dict1 = {
    #     "a": "ax",
    #     "b": "bx"
    # }
    # int1, int2 = funct8(3, 5)
    # print(int1)
    # print(int2)

    # func6(a="ax")
    # func6()

    # func1()
    # print(func2("my ", "string"))
    # func3()
    # print(factorial(3))
    # print(l1)
    # ml2()
    # ml2(l1)
    # ml2()
    # func4(10, d=3)
    # func4(10, 3)
    # func5(*l1)
    # func5(1, 2, 3)


garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"
message = filter(lambda x: x != "X", garbled)
print("".join(message))  # displays the list like a string
