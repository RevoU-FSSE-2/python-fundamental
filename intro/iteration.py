name = "alice" # string
keranjang = ["apel", "jeruk", "mangga"] # list

for huruf in name:
    print(huruf)

for buah in keranjang:
    print(buah)

# iterate with index
for index, buah in enumerate(keranjang):
    print(f"index {index} buah {buah}")

count = 0

while count < 10:
    print(count)
    count += 1