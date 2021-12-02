with open('input.txt') as f:
    steps = f.read().strip().split('\n')

horz, depth = 0,0
for inst in steps:
    mov_type, dist = inst.split()
    if mov_type=='forward':
        horz += int(dist)
    elif mov_type=='up':
        depth -= int(dist)
    elif mov_type=='down':
        depth += int(dist)

print(horz*depth)

horz, depth, aim = 0,0,0
for inst in steps:
    mov_type, dist = inst.split()
    if mov_type=='forward':
        horz, depth = horz+int(dist), depth+aim*int(dist)
    elif mov_type=='up':
        aim -= int(dist)
    elif mov_type=='down':
        aim += int(dist)

print(horz*depth)
