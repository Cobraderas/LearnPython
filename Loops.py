
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


print("Counting...")

for i in range(20):
    print(i)

