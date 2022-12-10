with open("input", "r") as f:
    data = f.read().strip().split("\n")


X, cycle, read_signal = 1,1,0
screen = [['.' for _ in range(40)] for _ in range(6)]
inst_ptr = 0
wait_cycle = False
for cycle in range(1,241):
    if cycle%40 == 20:
        read_signal += cycle*X
    crt_y, crt_x = divmod(cycle-1,40)
    screen[crt_y][crt_x] = '#' if crt_x in range(X-1,X+2) else '.'
    if wait_cycle:
        wait_cycle = False
        X += operand
    else:
        inst = data[inst_ptr]
        if inst == 'noop':
            inst_ptr += 1
        else:
            inst_ptr += 1
            wait_cycle = True
            operand = int(inst.split()[-1])


print(read_signal)
for row in screen:
    print("".join(row))


