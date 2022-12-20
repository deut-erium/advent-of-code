from itertools import cycle

with open("input", "r") as f:
    jetstream_s = f.read().strip()

import random
# jetstream_s = "".join(random.choices("<>",k=40))
len_js = len(jetstream_s)
# jetstream_s = ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"
jetstream = cycle(jetstream_s)
pieces = [
    [-1,0,1,2], # "####"
    [(-1+1j),(0),(1j),(1+1j),(2j)], # ".#.\n###\n.#."
    [(-1),(0),(1),(1+1j),(1+2j)], # "..#\n..#\n###"
    [(-1+0j),(-1+1j),(-1+2j),(-1+3j)],       # "#\n#\n#\n#"
    [(-1),(0),(-1+1j),(1j)]
    ]

tunnel = {i-1j:'_' for i in range(-4,5)}
MAX_HEIGHT = -1

def cycle_length(sequence):
    for i in range(1,len(sequence)):
        if all(sequence[:i]==sequence[k*i:(k+1)*i] for k in range(len(sequence)//i)):
            return i


def print_tunnel(tunnel,piece=[],jet_move="."):
    print(jet_move)
    tunnel_s = []
    for i in range(max(MAX_HEIGHT-10,0),MAX_HEIGHT+5):
        tunnel_s.append([tunnel.get(x+1j*i,"X" if x+1j*i in piece else '.') for x in range(-4,5)])
    for row in tunnel_s[::-1]:
        print("".join(row))

MAX_COUNT = len_js*300
MAX_TUNNEL_WINDOW = 15

def free_tunnel(tunnel):
    for i in list(tunnel.keys()):
        if i.real < MAX_HEIGHT-MAX_TUNNEL_WINDOW:
            del tunnel[i]


x = []
count = 0
for piece in cycle(pieces):
    if count%len_js == 0:
        print(MAX_HEIGHT+1)
        print_tunnel(tunnel,piece,'')
        x.append(MAX_HEIGHT+1)
        free_tunnel(tunnel)
    if count==MAX_COUNT:
        # print_tunnel(tunnel,piece,'')
        break
    count+=1
    start = (MAX_HEIGHT + 4)*1j
    piece = [i+start for i in piece]
    while True:
        jet_move = next(jetstream)
        if jet_move == "<":
            move_x = -1
        else:
            move_x = 1
        if any(i+move_x in tunnel or abs((i+move_x).real) >= 4 for i in piece): #if left or right cannot be done
            move_x = 0
        # _ = input()
        # print_tunnel(tunnel,piece,jet_move)
        if any(i+move_x-1j in tunnel for i in piece): #if the piece cant go down
            for i in piece:
                if i.imag > MAX_HEIGHT:  #make walls for new height
                    for h in range(MAX_HEIGHT,int(i.imag+1)):
                        tunnel[4+h*1j]='|'
                        tunnel[-4+h*1j]='|'
                    MAX_HEIGHT = int(i.imag)
                tunnel[i+move_x] = '#'
            break
        else:
            piece = [i+move_x-1j for i in piece]

print(MAX_HEIGHT+1)
diff_x = [i-j for i,j in zip(x[1:],x)]
mind = min(diff_x[1:])
diff_x = [i-mind for i in diff_x]
