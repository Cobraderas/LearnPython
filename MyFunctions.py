# def is_even(x):
#     if x % 2 == 0:
#         return True
#     else:
#         return False


# def is_int(x):
#     if x == int(x):
#         return True
#     else:
#         return False
#
#
# print(is_int(4.5))
# print(is_int(7))


# def digit_sum(n):
#     x = str(n)
#     y = 0
#     if n > 0:
#         for t in x:
#             y += int(t)
#         return y
#
#
# print(digit_sum(12345))


# def factorial(x):
#     total = 1
#     while x > 0:
#         total *= x
#         x -= 1
#     return total
#
#
# print(factorial(5))


# def is_prime(x):
#     if x < 2:
#         return False
#     if x == 2:
#         return True
#     for i in range(2, x):
#         if x % i == 0:
#             return False
#     else:
#         return True
#
#
# print(is_prime(105))
