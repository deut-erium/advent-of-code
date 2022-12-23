from itertools import cycle

with open("input", "r") as f:
    jetstream_s = f.read().strip()

# jetstream_s = ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"
jetstream = cycle(jetstream_s)
pieces = [
    (-1,0,1,2), # "####"
    ((-1+1j),(0),(1j),(1+1j),(2j)), # ".#.\n###\n.#."
    ((-1),(0),(1),(1+1j),(1+2j)), # "..#\n..#\n###"
    ((-1+0j),(-1+1j),(-1+2j),(-1+3j)),       # "#\n#\n#\n#"
    ((-1),(0),(-1+1j),(1j))
    ]

tunnel = {i-1j:'_' for i in range(-4,5)}
MAX_HEIGHT = -1

def print_tunnel(tunnel,piece=[],jet_move="."):
    print(jet_move)
    tunnel_s = []
    for i in range(max(MAX_HEIGHT-10,0),MAX_HEIGHT+5):
        tunnel_s.append([tunnel.get(x+1j*i,"X" if x+1j*i in piece else '.') for x in range(-4,5)])
    for row in tunnel_s[::-1]:
        print("".join(row))

MAX_TUNNEL_WINDOW = 17

def top_pattern(tunnel,piece):
    return frozenset(x+1j*(i-MAX_HEIGHT) for x in range(-4,5) for i in range(MAX_HEIGHT-MAX_TUNNEL_WINDOW,MAX_HEIGHT+1) if x+1j*i in tunnel),piece



MAX_COUNT = 1_000_000_000_000
# MAX_COUNT = 2022
# heights = {}
seen = {}

x = []
count = 0
while True:
    piece = pieces[count%5]
    if MAX_HEIGHT>MAX_TUNNEL_WINDOW:
        pattern = top_pattern(tunnel,piece)
        if pattern in seen:
            # if pattern not in heights:
                last_height,last_count = seen[pattern]
                height_diff, count_diff = MAX_HEIGHT-last_height, count-last_count

                num_count = (MAX_COUNT - count)//count_diff
                count += num_count*count_diff
                MAX_HEIGHT += height_diff*num_count
                # copy the top of tunnel
                for point in pattern[0]:
                    tunnel[point+1j*(MAX_HEIGHT)] = '#'
                # heights[pattern] = height_diff, count_diff
                # break
                # seen[pattern] = (MAX_HEIGHT,count)
            # else:
                # # just checking repetition
                # last_height,last_count = seen[pattern]
                # assert heights[pattern] == (MAX_HEIGHT-last_height, count-last_count)
                # seen[pattern] = (MAX_HEIGHT,count)
        else:
            seen[pattern] = (MAX_HEIGHT,count)
    if count==MAX_COUNT:
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
