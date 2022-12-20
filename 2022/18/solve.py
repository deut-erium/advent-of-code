from collections import deque
with open("input", "r") as f:
    data = f.read().strip()

# data = """2,2,2
# 1,2,2
# 3,2,2
# 2,1,2
# 2,3,2
# 2,2,1
# 2,2,3
# 2,2,4
# 2,2,6
# 1,2,5
# 3,2,5
# 2,1,5
# 2,3,5"""

cubes = [tuple(map(int,row.split(","))) for row in data.split()]

def adj(a):
    return [tuple(x+y for x,y in zip(a,i)) for i in ((0,0,1),(0,0,-1),(0,1,0),(0,-1,0),(1,0,0),(-1,0,0))]


INSIDE = set()
OUTSIDE = set()
SOLID = set(cubes)

def check_inside(point,INSIDE=INSIDE,OUTSIDE=OUTSIDE):
    if point in INSIDE:
        return True
    if point in OUTSIDE:
        return False
    q = deque([point])
    seen = set()
    while q:
        node = q.popleft()
        if node in SOLID:
            continue
        if node in seen:
            continue
        seen.add(node)
        if len(seen)>20*20*20:
            OUTSIDE|=seen
            return False
        q.extend(adj(node))
    INSIDE|=seen
    return True

TOTAL = 0
for i in cubes:
    for ad in adj(i):
        if ad not in SOLID and not check_inside(ad):
            TOTAL+=1

print(TOTAL)

