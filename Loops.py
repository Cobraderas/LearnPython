
# count = 0

# if count < 5:
#     print("Hello, I am an if statement and count is", count)

# while count < 5:
#     print("Hello, I am a while and count is", count)
#     count += 1


# num = 1

# while num <= 10:  # Fill in the condition
#     print(num ** 2)  # Print num squared
#     num += 1  # Increment num (make sure to do this!)

# choice = input('Enjoying the course? (y/n)')

# while choice != "y" and choice != "n":  # Fill in the condition (before the colon)
#     choice = input("Sorry, I didn't catch that. Enter again: ")


# count = 0

# while True:
#     print(count)
#     count += 1
#     if count >= 22:
#         break


# import random
#
# print("Lucky Numbers! 3 numbers will be generated.")
# print("If one of them is a '5', you lose!")
#
# count = 0
# while count < 3:
#     num = random.randint(1, 6)
#     print(num)
#     if num == 5:
#         print("Sorry, you lose!")
#         break
#     count += 1
# else:
#     print("You win!")


# from random import randint

# # Generates a number from 1 through 10 inclusive
# random_number = randint(1, 10)
#
# guesses_left = 3
# # Start your game!
# guess = int(input("Your guess: "))
# while guesses_left > 0:
#     num = random_number
#     print(num)
#     if guess == num:
#         print("You win!")
#         break
#     guesses_left -= 1
# else:
#     print("You lose!")


# print("Counting...")
#
# for i in range(20):
#     print(i)
#
# hobbies = []
#
# for i in range(3):
#     hobbi = input("Your hobbi is? :")
#     hobbies.append(str(hobbi))
# print(hobbies)


# thing = "spam!"
# for c in thing:
#     print(c)
# print("======")
# word = "eggs!"
#
# for a in word:
#     print(a)


# phrase = "A bird in the hand..."
#
# for char in phrase:
#     if char == "A" or char == "a":
#         print("X", end="")
#     else:
#         print(char, end="")
#
# # Don't delete this print statement!
# print


# numbers = [7, 9, 12, 54, 99]
#
# print("This list contains: ")
#
# for num in numbers:
#     print(num)
#
# for num in numbers:
#     print(num ** 2)


# d = {'a': 'apple', 'b': 'berry', 'c': 'cherry'}
#
# for key in d:
#     print(key, d[key])


# choices = ['pizza', 'pasta', 'salad', 'nachos']
#
# print('Your choices are:')
# for index, item in enumerate(choices):
#     print(index + 1, item)


# # zip will create pairs of elements when passed two lists, and will stop at the end of the shorter list.
# # zip can handle three or more lists as well!
# list_a = [3, 9, 17, 15, 19]
# list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]
#
# for a, b in zip(list_a, list_b):
#     if a > b:
#         print(a)
#     else:
#         print(b)


# # the else statement is executed after the for, but only if the for ends normally—that is, not with a break
# fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']
#
# print('You have...')
# for f in fruits:
#     if f == 'tomato':
#         print('A tomato is not a fruit!')  # (It actually is.)
#         break
#     print('A', f)
# else:
#     print('A fine selection of fruits!')

