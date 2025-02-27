data1 = [1, 2, 3, 4, 5]
data2 = [6, 2, 7, 4, 5]
data1set = set(data1)
data2set = set(data2)
# look for differences
# print(data2set.difference(data1set))

# look for similarities
# print(data2set.intersection(data1set))

# look for all data
# print(data2set.union(data1set))
uniondata = data2set.union(data1set) # {1, 2, 3, 4, 5, 6, 7}
print(data1set - data2set)
print(data2set - data1set)
uniondata.remove(4)
# print(uniondata)