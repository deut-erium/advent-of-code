with open("input") as f:
    data = f.read()

#data = """....#..
#..###.#
##...#.#
#.#...##
##.###..
###.#.##
#.#..#.."""

# data = """.....
# ..##.
# ..#..
# .....
# ..##.
# ....."""

grid = {(x,y):i  for y,row in enumerate(data.split()) for x,i in enumerate(row) if i=='#'}

DIR = {
        "N":  (0,-1),
        "NE": (1,-1),
        "E":  (1,0),
        "SE": (1,1),
        "S":  (0,1),
        "SW": (-1,1),
        "W":  (-1,0),
        "NW": (-1,-1)
    }

DIR_ORDER = "NSWE"
ADJ = {
        "N":("N","NE","NW"),
        "S":("S","SE","SW"),
        "W":("W","NW","SW"),
        "E":("E","SE","NE"),
      }

def move(pos, dir):
    (x,y),(i,j) = pos, DIR[dir]
    return x+i, y+j


def propose(pos, grid, round):
    if not any(grid.get(i,'.')=="#" for i in (move(pos,dir) for dir in DIR)):
        return None #dont move at all
    x,y = pos
    for i in range(4):
        next_dir = DIR_ORDER[(i+round)%4]
        if not any(grid.get(i,'.')=="#" for i in (move(pos,dir) for dir in ADJ[next_dir])):
            return move(pos,next_dir)

def dimensions(grid):
    min_x, max_x, min_y, max_y = float('inf'), -float('inf'), float('inf'), -float('inf')
    for x,y in grid:
        if x<min_x:
            min_x = x
        if x>max_x:
            max_x = x
        if y<min_y:
            min_y = y
        if y>max_y:
            max_y = y
    return (min_x, max_x, min_y, max_y)

def print_grid(grid):
    (min_x, max_x, min_y, max_y) = dimensions(grid)
    for y in range(min_y, max_y+1):
        print("".join(grid.get((x,y),'.') for x in range(min_x, max_x+1)))
    print()

last_moved = {i:0 for i in grid}

def round(grid,round_num):
    proposals = {}
    change = False
    for pos in grid:
        new_pos = propose(pos,grid,round_num%4)
        if new_pos:
            proposals.setdefault(new_pos,[]).append(pos)
    for i,v in proposals.items():
        if len(v)==1:
            change = True
            grid[i] = '#'
            del grid[v[0]]
    return change

round_num = 0
while True:
    # if round_num==10: #part 1
    #     break
    if not round(grid,round_num):
        break
    round_num+=1
    # print_grid(grid)

x_min,x_max,y_min,y_max = dimensions(grid)
print((x_max-x_min+1)*(y_max-y_min+1) - len(grid))
print("round_num",round_num+1)
