with open("input", "r") as f:
    data = f.read().strip()

# data = """498,4 -> 498,6 -> 496,6
# 503,4 -> 502,4 -> 502,9 -> 494,9"""

lines = []
for line_s in data.split("\n"):
    line = []
    for xy in line_s.strip().split(" -> "):
        x,y = map(int, xy.split(","))
        line.append((x,y))
    lines.append(line)

cave = {}
for line in lines:
    for (x0,y0),(x1,y1) in zip(line,line[1:]):
        if x0==x1:
            for y in range(min(y0,y1), max(y0,y1)+1):
                cave[(x0,y)] = "#"
        else:
            for x in range(min(x0,x1), max(x0,x1)+1):
                cave[(x,y0)] = "#"

MAX_Y = max([i[1] for i in cave])
FLOOR = MAX_Y + 2

def print_cave(cave,xy=None):
    print()
    MIN_X = min([i[0] for i in cave])
    MAX_X = max([i[0] for i in cave])
    MIN_Y = min([i[1] for i in cave])
    MAX_Y = max([i[1] for i in cave])
    cave_p = [['.' for _ in range(MAX_X-MIN_X+1)] for _ in range(MAX_Y-MIN_Y+1)]
    for (x,y),v in cave.items():
        cave_p[y-MIN_Y][x-MIN_X] = v
    if xy and (y>=MIN_Y) and (x>=MIN_X):
        x,y = xy
        cave_p[y-MIN_Y][x-MIN_X] = 'X'
    for row in cave_p:
        print("".join(row))

def fill_sand(cave):
    next_x, next_y = 500,0
    while True:
        # print_cave(cave,(next_x,next_y))
        # _ = input()
        # if next_y > MAX_Y: #PART 1
        if cave.get((next_x,next_y),'.') != '.':
            return False
        if next_y == FLOOR-1:
            cave[(next_x,next_y)] = 'P'
            return True
        if cave.get((next_x,next_y+1),'.')=='.':
            next_y +=1
            continue
        elif cave.get((next_x-1,next_y+1),'.')=='.':
            next_x, next_y = next_x-1, next_y+1
            continue
        elif cave.get((next_x+1,next_y+1),'.')=='.':
            next_x, next_y = next_x+1, next_y+1
            continue
        else:
            cave[(next_x,next_y)] = 'O'
            break
    return True

count = 0
while True:
    if not fill_sand(cave):
        break
    count+=1

print(count)
