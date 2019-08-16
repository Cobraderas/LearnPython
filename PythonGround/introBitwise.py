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


# print(bin(1))
# print(bin(2))
# print(bin(3))
# print(bin(4))
# print(bin(5))
#
# print(hex(6))
#
# print(oct(7))


#  ===========================================================================================================
# int() function can turn non-integer input into an integer
# int function has an optional second parameter
# When given a string containing a number and the base that number is in,
# the function will return the value of that number converted to base ten

# print(int("1", 2))
# print(int("10", 2))
# print(int("111", 2))
# print(int("0b100", 2))
# print(int(bin(5), 2))
# # Print out the decimal equivalent of the binary 11001001.
# print(int("11001001", 2))


# shift_right = 0b1100
# shift_left = 0b1
#
# shift_right = shift_right >> 2
# shift_left = shift_left << 2
#
# print(bin(shift_right))
# print(bin(shift_left))


#  bitwise AND (&) operator compares two numbers on a bit level and returns
#  a number where the bits of that number are turned on if the corresponding
#  bits of both numbers are 1
#
# print(bin(0b1110 & 0b101))
# print(int("0b100", 2))


# bitwise OR (|) operator compares two numbers on a bit level and returns a
# number where the bits of that number are turned on if either of the
# corresponding bits of either number are 1
#
# print(bin(0b1110 | 0b101))


# XOR (^) or exclusive or operator compares two numbers on a bit level
# and returns a number where the bits of that number are turned on
# if either of the corresponding bits of the two numbers are 1, but not both
#
# print(bin(0b1110 ^ 0b101))


# bitwise NOT operator (~) just flips all of the bits in a single number
# print(~1)
# print(~2)
# print(~3)
# print(~42)
# print(~123)


# def check_bit4(number):
#     mask = 0b1000
#     desired = number & mask
#     if desired > 0:
#         return "on"
#     else:
#         return "off"
#
#
# print(check_bit4(0b0100))
# print(check_bit4(0b1100))
# print(check_bit4(0b1000))


# You can also use masks to turn a bit in a number on using |.
# For example, let’s say I want to make sure the rightmost bit of number a is turned on
# a = 0b10111011
# mask = 0b101111
# desired = a | mask
#
# print(bin(desired))


# Using the XOR (^) operator is very useful for flipping bits.
# Using ^ on a bit with the number one will return a result where that bit is flipped
# a = 0b11101110
# mask = 0b11111111
# desired = a ^ mask
#
# print(bin(desired))  # prints 0b10001


# def flip_bit(number, n):
#     mask = 0b1 << (n - 1)
#     result = number ^ mask
#     return bin(result)
#
#
# print(flip_bit(0b10111, 1))
