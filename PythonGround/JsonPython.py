# Parse JSON - convert from JSON to Python
import json

# some JSON:
x = '{ "name":"John", "age":"30", "city":"New York" }'

# parse x
y = json.loads(x)

# the result is a python dictionary
print(y["age"])


# convert from python to json

# a python object (dict):
x = {
    "name": "John",
    "age": "30",
    "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string
print(y)

print(" ================================== ")

z = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(z))
print(" ================================== ")

print(json.dumps(z, indent=4))
print(" ================================== ")

print(json.dumps(z, indent=4, separators=(". ", " = ")))
print(" ================================== ")

print(json.dumps(z, indent=4, sort_keys=False))



