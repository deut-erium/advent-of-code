import string
with open("input", "r") as f:
    rucksacks = f.read().strip().split()

ITEMS = string.ascii_lowercase + string.ascii_uppercase
PRIORITY = {v:i+1 for i,v in enumerate(ITEMS)}

total_priority = 0
for i in rucksacks:
    common_char = set(i[:len(i)//2]).intersection(set(i[len(i)//2:])).pop()
    total_priority += PRIORITY[common_char]

print(total_priority)


# PART TWO
total_priority_2 = 0
for i in range(0, len(rucksacks), 3):
    e1, e2, e3 = rucksacks[i:i+3]
    badge = set(e1).intersection(set(e2)).intersection(set(e3)).pop()
    total_priority_2 += PRIORITY[badge]
print(total_priority_2)





