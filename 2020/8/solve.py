with open('input.txt') as f:
    data = f.read().strip().split('\n')
    data = [i.split() for i in data]

instructions = [(i[0],int(i[1])) for i in data]
acc = 0
inst = 0
seen = set()
while True:
    if inst in seen:
        inst+=1
    seen.add(inst)
    print(instructions[inst])
    typ, op = instructions[inst]
    if typ=='nop':
        inst+=1
    elif typ=='acc':
        acc+=op
        inst+=1
    elif typ=='jmp':
        inst+=op

