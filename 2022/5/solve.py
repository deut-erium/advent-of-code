import re
with open("input", "r") as f:
    stacks_s, operations_s = f.read().strip().split("\n\n")
    stacks_s = stacks_s.split("\n")
    operations = [list(map(int,i)) for i in re.findall("move (\d+) from (\d+) to (\d+)",operations_s)]

num_stacks = (len(stacks_s[-1]) + 1)//4
stacks = [[] for _ in range(num_stacks)]

for row in stacks_s[:-1][::-1]:
    for i in range(9):
        if (crate:=row[4*i+1])!=' ':
            stacks[i].append(crate)

# PART 1
# for num, start, end in operations:
#     for _ in range(num):
#         stacks[end-1].append(stacks[start-1].pop())

# PART 2
for num, start, end in operations:
    stacks[end-1].extend(stacks[start-1][-num:])
    stacks[start-1] = stacks[start-1][:-num]

print("".join(i[-1] for i in stacks))
