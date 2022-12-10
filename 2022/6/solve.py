import string
with open("input", "r") as f:
    data = f.read().strip()

WIN_SIZE = 4 # 14 for PART 2
for i in range(len(data)-WIN_SIZE):
    if len(set(data[i:i+WIN_SIZE]))==WIN_SIZE:
        break
print(i+WIN_SIZE)


