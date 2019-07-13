# Consider a module to be the same as a code library.
# A file containing a set of functions you want to include in your application.
# To create a module just save the code you want in a file with the file extension .py
# To import easily the module make sure is in the root of your project else give also the folder path

import mymodule
import platform

mymodule.greeting("Johnathan")

a = mymodule.person1["age"]
print(a)

# you can rename a module (create an alias) using the as keyword
# ex:
# from  PythonGround import mymodule as HH

x = platform.system()
print(x)

# there is a built in function to list all the function names (or available names)
# in a module. the dir() function

x = dir(platform)
print(x)

print(" ")

# import a dictionary from custom module (should be on top but i ignored that)
from mymodule import person1

print(person1["age"])
