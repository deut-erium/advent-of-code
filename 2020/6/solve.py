with open('input.txt') as f:
    groups = f.read().strip().split('\n\n')

total_all, total_any = 0,0
for group in groups:
    answered_any = set()
    answered_all = set('abcdefghijklmnopqrstuvwxyz')
    for line in group.split():
        answered_any |= set(line)
        answered_all &= set(line)
    total_all+=len(answered_all)
    total_any+=len(answered_any)

print(total_any)
print(total_all)
