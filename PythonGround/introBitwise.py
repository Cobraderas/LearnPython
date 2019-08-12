# garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"
# message = filter(lambda x: x != "X", garbled)
# print("".join(message))  # displays the list like a string
# print(message)


# one = 0b1
# two = 0b10
# three = 0b11
# four = 0b100
# five = 0b101
# six = 0b110
# seven = 0b111
# eight = 0b1000
# nine = 0b1001
# ten = 0b1010
# eleven = 0b1011
# twelve = 0b1100


# There are Python functions that can aid you with bitwise operations. In order to print a number in its binary
# representation, you can use the bin() function. bin() takes an integer as input and returns the binary representation
# of that integer in a string.
# (Keep in mind that after using the bin function, you can no longer operate on the value like a number.)
#
# You can also represent numbers in base 8 and base 16 using the oct() and hex() functions.


print(bin(1))
print(bin(2))
print(bin(3))
print(bin(4))
print(bin(5))

print(hex(6))

print(oct(7))
