# json operations and methods

# json_text = r'{"alphabet": [{"abc" : {"a": 1.0, "b": 2.0, "c": 3.0}}, {"def" : {"d": 4, "e": 5, "f": 6}}]}'

# import json
#
# json_text = r'{"alphabet": [{"abc" : {"a": 1.0, "b": 2.0, "c": 3.0}}, {"def" : {"d": 4, "e": 5, "f": 6}}]}'
#
# # loads
# json_obj = json.loads(json_text)
# print(type(json_obj))
#
# print(json_obj["alphabet"])
# print(json_obj["alphabet"][0])
# print(json_obj["alphabet"][0]["abc"]["b"])
#
#
# json_obj = json.loads(json_text, parse_int=lambda e: int(e) * 10)
# print(json_obj)
#
# json_obj = json.loads(json_text, parse_float=lambda e: float(e) * 15)
# print(json_obj)
#
#
# json_text2 = r'{"m_inf": -Infinity, "inf": Infinity, "nan": NaN}'
#
#
# def parse_js_const(input):
#     if input == "-Infinity":
#         return float('-inf')
#     elif input == "Infinity":
#         return float('inf')
#     elif input == "NaN":
#         return float('nan')
#
#
# json_obj2 = json.loads(json_text2, parse_constant=parse_js_const)
# print(json_obj2)
#
# print("-" * 100)
#
# # load
#
# with open("input.json") as f:
#     json_obj = json.load(f)
#     print(json_obj)
#
# # dumps - makes the json a string
#
# json_dump = json.dumps(json_obj)
# print(type(json_dump))
# print(json_dump)
#
# print("-" * 100)
# # dump - saves json to file
#
# with open("output.json", "w+") as f:
#     # json.dump(json_obj2, f)
#     json.dump(json_obj2, f, allow_nan=True)
#
# print(json_obj)
# json_obj.append(json.loads(r'{"x": 123}'))
# print(json_obj)
# with open("output.json", "w+") as f:
#     json.dump(json_obj, f, allow_nan=True)
#
#
# print("-" * 100)


# csv
import csv
f = open("input.csv")
reader = csv.reader(f, delimiter=";")  # iterator
for line in reader:
    print(line)


print("-" * 100)

