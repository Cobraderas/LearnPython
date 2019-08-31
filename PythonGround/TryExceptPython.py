# The try block will generate an exception, because x is not defined:
try:
    print(x)
except:
    print("Exception occurred")

# You can define as many exception blocks as you want, e.g. if you want to execute a special block
# of code for a special kind of error
# Print one message if the try block raises a NameError and another for other errors:

try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")

print(" =========== ")

try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")

# The finally block, if specified, will be executed regardless if the try block raises an error or not.
try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("The 'try except' is finished")


# Try to open and write to a file that is not writable
# finally:  can be useful to close objects and clean up resources

try:
    f = open("demofile.txt")
    f.write("Lorum Ipsum")
except:
    print("Something went wrong when writing to the file")
finally:
    f.close()


