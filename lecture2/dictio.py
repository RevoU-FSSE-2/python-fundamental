person = {
    "name": "John",
    "age": 25,
    "height": 180.5,
    "is_student": True,
    "aliases": ["tewel", "jons", "jojo"],
}

person2 = {
    "name": "Jane",
    "age": 23,
    "height": 170.5,
    "is_student": False,
    "aliases": ["jane", "janny", "jane"],
}
kangaroo = {
    "height": 180.5,
    "weight": 70.5,
    "food": ["grass", "leaf", "bark"],
}
# iterable is list, tuple, set, dictionary, string

# print(person["name"])
# print(person["nama"]) # KeyError
# print(person.get("name")) # safe access
# print(person.get("nama")) # None
# print(person.get("nama", "unkown")) # safe access with default value
variable_yang_akan_digunakan_nanti = list(kangaroo.values())
for key in kangaroo:
    print(key)

for value in kangaroo.values():
    print(value, "<<", type(value))

for key, value in kangaroo.items():
    print(key, ":", value)
try:
    kangaroo["amount"] = 190.5
except KeyError as e:
    print(e)