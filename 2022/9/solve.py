with open("input", "r") as f:
    data = []
    for line in f.read().strip().split("\n"):
        dir, step = line.split()
        data.append(("RULD".index(dir), int(step)))

moves = {1+2j:   1+1j,
         1-2j:   1-1j,
         2+1j:   1+1j,
         2-1j:   1-1j,
         -1+2j: -1+1j,
         -1-2j: -1-1j,
         -2+1j: -1+1j,
         -2-1j: -1-1j,
         2+2j:   1+1j,
         -2-2j: -1-1j,
         2-2j:   1-1j,
         -2+2j: -1+1j,
         2:         1,
         1+1j:      0,
         2j:       1j,
         -2:       -1,
         -1+1j:     0,
         -2j:     -1j,
         -1-1j:     0,
         -2j:     -1j,
         1-1j:      0,
         1:         0,
         1j:        0,
         -1:        0,
         -1j:       0,
         0j:        0}

LEN = 10
rope = [0]*LEN
seen = set()
for dir, steps in data:
    for _ in range(steps):
        rope[0] += (1j)**dir
        for j in range(1,LEN):
            rope[j] += moves[rope[j-1]-rope[j]]
        seen.add(rope[-1])

print(len(seen))
