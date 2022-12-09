with open("input","r") as f:
    data = f.read()

elves_str = data.split("\n\n")
elves = [list(map(int,i.split())) for i in elves_str]
elves_total = list(map(sum,elves))
elves_sorted = sorted(elves_total)

print(elves_sorted[-1])
print(sum(elves_sorted[-3:]))

