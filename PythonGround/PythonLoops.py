# while loops

i = 1
while i < 6:
    print(i)
    i += 1
print("")

i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1
print("")

i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
print("")
print("==================================")

# for loops

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
print(" ")

fruits = ["apple", "banana", "cherry"]
for x in "banana":
    print(x)
print(" ")

# exit loop when x is banana
for x in fruits:
    print(x)
    if x == "banana":
        break
print(" ")

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)
print(" ")

# the continue statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:             # do not  print banana
    if x == "banana":
        continue
    print(x)
print(" ")

# the range() function usage
for x in range(6):
    print(x)
print(" ")

for x in range(2, 6):
    print(x)
print(" ")

for x in range(2, 30, 3):
    print(x)
print(" ")

for x in range(6):
    print(x)
else:
    print("Finally finished!")
print(" ")

# nested loop usage
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
    for y in fruits:
        print(x, y)
print(" ")


# recursive function usage
def tri_recursion(k):
    if k > 0:
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result


print("\n\nRecursion Example Results")
tri_recursion(20)
print(" ")
