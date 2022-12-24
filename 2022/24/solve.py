from math import lcm
from collections import deque
with open("input") as f:
    data = f.read()

#data = """#.######
##>>.<^<#
##.<..<<#
##>v.><>#
##<^v^^>#
#######.#"""

grid = {x+1j*y:v for y,row in enumerate(data.split()) for x,v in enumerate(row)}

X_MAX = int(max(i.real for i in grid))
Y_MAX = int(max(i.imag for i in grid))

CYCLE = lcm(X_MAX-1,Y_MAX-1)

for x in range(X_MAX):
    if grid[x]=='.':
        START = x

for y in range(X_MAX):
    if grid[y+1j*Y_MAX]=='.':
        END = y+1j*Y_MAX

def move(point, dir):
    x,y = map(int,(point.real,point.imag))
    dirx,diry = map(int,(dir.real,dir.imag))
    x_next = 1+(x-1+dirx)%(X_MAX-1)
    y_next = 1+(y-1+diry)%(Y_MAX-1)
    return complex(x_next,y_next)

DIRS = ">v<^"
bliz = {i:1j**(DIRS.index(v)) for i,v in grid.items() if v in DIRS}
border = {i:v if v=='#' else '.' for i,v in grid.items()}
BLIZZARDS = []
for cyc in range(CYCLE):
    BLIZZARDS.append(border|{move(i,v*cyc):'X' for i,v in bliz.items()})

def bfs(start,end,start_time=0):
    seen = {(start,start_time%CYCLE)}
    queue = deque([(start,start_time)])
    while queue:
        pos, depth = queue.popleft()
        if pos==end:
            return depth
        for adj in [pos+i for i in (0,1,-1,1j,-1j)]:
            if BLIZZARDS[(depth+1)%CYCLE].get(adj,'#')=='.' and (adj,(depth+1)%CYCLE) not in seen:
                seen.add((adj,(depth+1)%CYCLE))
                queue.append((adj,depth+1))

reach_time = bfs(START,END,0)
print(reach_time)
start_reach_time = bfs(END, START, reach_time)
print(start_reach_time)
final_reach_time = bfs(START, END, start_reach_time)
print(final_reach_time)

