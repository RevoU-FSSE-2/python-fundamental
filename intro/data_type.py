# dynamic typing data type

name = "John" # string
age = 25 # integer
height = 180.5 # float
is_student = True # boolean
aliases = ["tewel", "jons", "jojo"] # list
address = ("New York", "USA") # tuple
scores = {"math": 90, "physics": 85, "chemistry": 80} # dictionary
absent = {"2024-01-01", "2024-01-02", "2024-01-03"} # set

print(type(name)) # <class 'str'>
print(type(age)) # <class 'int'>
print(type(height)) # <class 'float'>
print(type(is_student)) # <class 'bool'>
print(type(aliases)) # <class 'list'>
print(type(address)) # <class 'tuple'>
print(type(scores)) # <class 'dict'>
print(type(absent)) # <class 'set'>

# standard output
print(name, "is", age, "years old and", height, "cm tall.")
print(name + "is")

# string interpolation / formatting
print(f"{name} is {age} years old and {height} cm tall.")
print(f"has aliases: {aliases}")
print(f"alias first is {aliases[0]} and alias second is {aliases[1]}")
print(f"lives in {address[0]}, {address[1]}")
print(f"has scores: {scores}")
print(f"absent on: {absent}")

# interacting with list
aliases.append("idruss") # add new element
print(f"has aliases: {aliases}")
print(f"first alias: {aliases[0]}") # index
print(f"last alias: {aliases[-1]}") # negative index  == last element
print(f"total aliases: {len(aliases)}") # length of list
# interacting with tuple
address = address + ("12345",)

print(address)
aliases[3] = "pepe" # update element
print(aliases)
# tuple is immutable
# address[2] = "Los Angeles" # error

print(f"lives in {address[0]}, {address[1]}, {address[2]}")

# interacting with dictionary
print(f"math score: {scores['math']}") # key access
scores["math"] = 95 # update value
print(scores)
scores["english"] = 88 # add new key-value pair
print(f"has scores: {scores}")


# interacting with set
# set is unordered and unique
absent.add("2024-01-04") # add new element
print(f"absent on: {absent}")
absent.add("2024-01-04") # no effect
print(f"absent on: {absent}")
absent.add("2024-01-01") # add new element
print(f"absent on: {absent}")   