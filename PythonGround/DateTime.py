import datetime

x = datetime.datetime.now()
print(x)
print(x.year)
print(x.strftime("%A"))

# create date object
x = datetime.datetime(2020, 5, 17)
print(x)

# The datetime object has a method for formatting date objects into readable strings.
# The method is called strftime(), and takes one parameter, format, to specify the format of the returned string:

x = datetime.datetime(2018, 6, 1)
print(x.strftime("%B"))
print(x.strftime("%c"))
print(x.strftime("%%"))
print(x.strftime("%U"))
print(x.strftime("%j"))


