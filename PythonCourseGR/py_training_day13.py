# input and exceptions

# in_value = input("Insert number: ")

# in_value = list(input("Insert letters separated by space: ").split())
# print(in_value)


# in_value = list(map(int, input("Insert letters separated by space: ").split()))
# print(in_value)

# try:
#     in_value = int(in_value)
# except Exception as err:
#     print(err)


# try:
#     in_value = int(in_value)
# except ValueError as err:
#     print(err)
# else:
#     print("No error!")

#
# try:
#     in_value = int(in_value)
#     f = open("no_file")
# except ValueError as err:
#     print(err)
# except FileNotFoundError as err:
#     print("Unknown error!")
#     raise

#
# try:
#     f = open("py_training_day12.py")
# except FileNotFoundError as err:
#     print(err)
# else:
#     print(f.readline())
# finally:
#     print("cleanup")
#     f.close()

# if True:
#     raise Exception(":D")
# print("ceva")  # does not run


# a valid line should look like [key=value]
class Parser:

    def __init__(self, line):
        sp_line = line.split("=")
        self.data = dict([(sp_line[0], sp_line[1])])
        #  self.data = {}
        #  self.data[sp_line[0]] = spline[1]

    def __str__(self):
        return str(self.data.items())


class ParseError(Exception):

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return "ParseError: {}".format(self.message)


class ContentError(Exception):
    def __init__(self, message, context):
        self.message = message
        self.context = context

    def __str__(self):
        return "ContextError {}\nError in line: {}".format(self.message, self.context)


def parse_line(line):
    if "[" not in line and "]" not in line:
        raise ParseError("Invalid line")
    elif len(line.split("= ")) != 2:
        raise ContentError("Invalid data format", line)
    else:
        return Parser(line)


if __name__ == "__name__":
    our_line = "asdf"
    try:
        result = parse_line(our_line)
    except ParseError as err:
        print(err)
    except ContentError as err:
        print(err)
    else:
        print(result)

