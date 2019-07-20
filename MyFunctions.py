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


# def reverse(text):
#     scris = ''
#     for i in text:
#         scris = i + scris
#     return scris
#
#
# print(reverse('market'))


# def reverse(text):
#     for i in range(len(text) - 1, -1, -1):
#         print(text[i], end='')
#
#
# reverse("farfurie")


# def anti_vowel(text):
#     vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
#     for i in text:
#         if i in vowels:
#             text = text.replace(i, '')
#     return text
#
#
# print(anti_vowel('paranoia'))


# def anti_vowel(text):
#     result = ""
#     vowels = "ieaouIEAOU"
#     for char in text:
#           if char not in vowels:
#             result += char
#     return result
#
#
# print(anti_vowel("hello book"))


score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}

# def scrabble_score(word):
