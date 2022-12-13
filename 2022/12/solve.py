from collections import deque
with open("input", "r") as f:
    terrain = f.read().strip().split()

terrain = {x+y*1j:ord(v) for y,row in enumerate(terrain) for x,v in enumerate(row)}

for key,value in terrain.items():
    if value == ord('S'):
        start = key
        terrain[key] = ord('a')
    if value == ord('E'):
        terrain[key] = ord('z')
        end = key

def search(start, end):
    seen = {}
    q = deque([(0, start)])
    while q:
        dist, node = q.popleft()
        if node in seen:
            continue
        seen[node] = dist
        for k in range(4):
            next_node = node+1j**k
            if terrain.get(next_node, float('inf')) - terrain[node] <=1:
                q.append((dist+1, next_node))
    if end in seen:
        return seen[end]
    return float('inf')

print(search(start,end))
print(min(search(i,end) for i,v in terrain.items() if v==ord('a')))

