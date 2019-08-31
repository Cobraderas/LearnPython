# format() method allows you to format selected parts of a string
# To control such values, add placeholders (curly brackets {})
# in the text, and run the values through the format() method:
price = 99
txt = "The price is {} euro"
print(txt.format(price))


# You can add parameters inside the curly brackets to specify how to convert the value
price = 99
txt = "The price is {:.2f} euro"
print(txt.format(price))


# want to use more values, just add more values to the format() method
# print(txt.format(price, itemno, count))
quantity = 5
itemno = 789
price = 99
myorder = "I want {} pieces of item no: {} for {:.2f} euro"
print(myorder.format(quantity, itemno, price))


# You can use index numbers (a number inside the curly brackets {0})
# to be sure the values are placed in the correct placeholders
quantity = 5
itemno = 789
price = 99
myorder = "I want {0} pieces of item no: {1} for {2:.2f} euro"
print(myorder.format(quantity, itemno, price))


# Also, if you want to refer to the same value more than once, use the index number:
age = 88
name = "Gogu"
text = "My name is {1}. {1} is {0} years old"
print(text.format(age, name))


# You can also use named indexes by entering a name inside the curly brackets {carname},
# but then you must use names when you pass the parameter values txt.format(carname = "Ford")

myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname="Dacia", model="Logan"))
