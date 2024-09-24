import sys
numbers = [1, 2, 3, 4, 5]
print(f"{numbers=}")
fixed_numbers = (1, 2, 3, 4, 5)
print(sys.getsizeof(numbers), "bytes")
print(sys.getsizeof(fixed_numbers), "bytes")

numbers.append(6) # append will add 6 to the end of the list
print(numbers, "added 6")
numbers.insert(0, 0) # insert will add 0 at index 0
print(numbers, "added at index 0")
numbers.remove(3)   # remove will remove the first occurrence of 3
print(numbers, "removed 3")
numbers.append(5)
print(numbers, "added 5")
numbers.remove(5)   # remove will remove the first occurrence of 5
print(numbers, "removed 5")
numbers.pop(2)     # pop will remove the element at index 2
print(numbers, "removed index 2")
numbers.pop()      # pop will remove the last element
print(numbers, "removed last element")

names = ["Alice", "Bob", "Charlie"]
names_tuple = tuple(names)
duplicated_names = ["Alice", "Bob", "Charlie", "Alice", "Bob", "Charlie"]
# print(names[1:3])
names[0] = "Alicia"
print(names, "changed index 0")
for name in names:
    print(name)
    if name == "Bob":
        break

for tname in names_tuple:
    print(tname)

print(duplicated_names, "<< duplicated names from list")

filtered_names = set(duplicated_names)
print(filtered_names, "<< filtered names from list")
filtered_names.remove("Alice")
filtered_names_aslist = list(filtered_names)
print(filtered_names_aslist)
