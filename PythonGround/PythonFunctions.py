# Functions usage


def my_function():
    print("Hello from a function")


my_function()
print(" ")


# function parameters usage
def my_function(fname):
    print(fname + " Refsnes")


my_function("Emil")
my_function("Tobias")
my_function("Linus")
print(" ")


# function default parameter value usage
def my_function(country="Norway"):
    print("I am from " + country)


my_function("Sweeden")
my_function("India")
my_function()
my_function("Africania")
print(" ")


# function return values
def my_function(x):
    return 5 * x


print(my_function(3))
print(my_function(5))
print(my_function(9))
print(" ")


# lambda function usage syntax:  lambda arguments : expression
x = lambda a: a + 10
print(x(5))
print(" ")

x = lambda a, b: a * b
print(x(5, 6))
print(" ")

x = lambda a, b, c: a + b + c
print(x(5, 6, 2))
print("==============================")


def myfunc(n):
    return lambda a: a * n


mydoubler = myfunc(2)
print(mydoubler(11))
print(" ")

# add some stuff
# lets commit?


def myfunc(n):
    return lambda a: a *n


mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))
print(" ")
