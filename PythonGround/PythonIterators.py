# an iterator is an object which implements the iterator protocol, which consists of the methods __iter__()
# and __next__()


# return an iterator from tuple, and print each value
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

print(" ")

mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

print(" ")

# iterate the values of a tuple
mytuple = ("apple", "banana", "cherry")

for x in mytuple:
    print(x)

print(" ")

mystring = "caledonia"

for x in mystring:
    print(x)

print(" ")

# Create an Iterator
# To create an object/class as an iterator you have to implement the methods __iter__() and __next__() to your object.
# As you have learned in the Python Classes/Objects chapter, all classes have a function called __init__(),
# which allows you do some initializing when the object is being created.
# The __iter__() method acts similar, you can do operations (initializing etc.), but must always return the
# iterator object itself.
# The __next__() method also allows you to do operations, and must return the next item in the sequence.


class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x


myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

print(" ")

# stop after 20 iterations
class MyNumbersa:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


myclassa = MyNumbersa()
myitera = iter(myclassa)

for x in myitera:
    print(x)




