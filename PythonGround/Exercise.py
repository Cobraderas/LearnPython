# Python if...else
# if usage
a = 33
b = 200
if b > a:
    print('b is greater than a')

# elif usage
a = 33
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")

# else usage
a = 200
b = 33
c = 201
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")

# shorthand if
if a > b: print("a is greater than b")

# shorthand if else
print("A") if a > b else print("B")

# multiple if else on one line
print("A") if a > b else print("=") if a == b \
    else print("B")

# and keyword chained
if a > b and c > a:
    print("both cond are true")

# or keyword usage
if a > b or a > c:
    print("At least one of the conditions are True")
