

# creates a class
class MyClass:
    x = 5


# create an object and print the class variable
p1 = MyClass()
print(p1.x)
print(" ")

# the _init_() function
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("John", 36)

print(p1.name)
print(p1.age)
print(" ")
# __init__() function is called automatically every time the class is being used
# to create a new object.


# creates a method within an object
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myFunc(self):
        print("Hello my name is " + self.name)


p1 = Human("John", 33)
p1.myFunc()
print(" ")
# The self parameter is a reference to the class instance itself, and is used
# to access variables that belongs to the class

class Alien:
    def __init__(someObject, name, age):
        someObject.name = name
        someObject.age = age

    def myfunc(abc):
        print("Hello my name is " + abc.name)


p1 = Alien("Johan", 36)
p1.myfunc()

# modify object properties
p1.age = 40


# delete object properties
del p1.age


# delete objects
del p1

print(" ")

class Person:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age

    def myfunc(self):
        print("Hello my name is " + self.name + " " + str(self.age) + " years")


p1 = Person("John", 36)
p1.myfunc()
