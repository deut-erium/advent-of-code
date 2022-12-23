import re
with open("input") as f:
    data = f.read()

#data = """        ...#
#        .#..
#        #...
#        ....
#...#.......#
#........#...
#..#....#....
#..........#.
#        ...#....
#        .....#..
#        .#......
#        ......#.

#10R5L5R10L4R5L5"""
grid, steps = data.split("\n\n")

grid = {(x,y):v for y,row in enumerate(grid.split("\n")) for x,v in enumerate(row) if v in "#."}

x_min, x_max, y_min, y_max = float('inf'), -float('inf'), float('inf'), -float('inf')
for (x,y) in grid:
    if x > x_max:
        x_max = x
    if x < x_min:
        x_min = x
    if y > y_max:
        y_max = y
    if y < y_min:
        y_min = y

boundaries_xmin = {}
boundaries_xmax = {}
for x in range(x_min, x_max+1):
    min_xy = min(y for y in range(y_min, y_max+1) if (x,y) in grid)
    max_xy = max(y for y in range(y_min, y_max+1) if (x,y) in grid)
    boundaries_xmin[x], boundaries_xmax[x] = min_xy, max_xy

boundaries_ymax = {}
boundaries_ymin = {}
for y in range(y_min, y_max+1):
    min_yx = min(x for x in range(x_min, x_max+1) if (x,y) in grid)
    max_yx = max(x for x in range(x_min, x_max+1) if (x,y) in grid)
    boundaries_ymin[y], boundaries_ymax[y] = min_yx, max_yx


def rotate(facing, step):
    new_face = complex(*facing)*{"R":1j,"L":-1j}[step]
    return int(new_face.real),int(new_face.imag)

def wrap1(x,y,facing):
    if facing[0]:
        return ((x+facing[0]-boundaries_ymin[y])%(boundaries_ymax[y]-boundaries_ymin[y]+1)+boundaries_ymin[y], y),facing
    return (x,(y+facing[1]-boundaries_xmin[x])%(boundaries_xmax[x]-boundaries_xmin[x]+1)+boundaries_xmin[x]),facing


x,y,facing = boundaries_ymin[y_min],y_min,(1,0)
steps = re.findall("(\d+|L|R)",steps)
for step in steps:
    # print(x,y,step)
    if step in "LR":
        facing = rotate(facing, step)
        # print("\tfacing", facing)
    else:
        for n in range(int(step)):
            # print("\tstep",x,y)
            (x1,y1),facing = wrap1(x,y,facing)
            if grid[(x1,y1)] == '#':
                break
            x,y = x1,y1
    # print(x,y)
print(1000*(y+1)+4*(x+1)+{(1,0):0,(0,1):1,(-1,0):2,(0,-1):3}[facing])
