import re
from itertools import combinations
from collections import Counter
with open("input") as f:
    data = f.read()

# data = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
# Sensor at x=9, y=16: closest beacon is at x=10, y=16
# Sensor at x=13, y=2: closest beacon is at x=15, y=3
# Sensor at x=12, y=14: closest beacon is at x=10, y=16
# Sensor at x=10, y=20: closest beacon is at x=10, y=16
# Sensor at x=14, y=17: closest beacon is at x=10, y=16
# Sensor at x=8, y=7: closest beacon is at x=2, y=10
# Sensor at x=2, y=0: closest beacon is at x=2, y=10
# Sensor at x=0, y=11: closest beacon is at x=2, y=10
# Sensor at x=20, y=14: closest beacon is at x=25, y=17
# Sensor at x=17, y=20: closest beacon is at x=21, y=22
# Sensor at x=16, y=7: closest beacon is at x=15, y=3
# Sensor at x=14, y=3: closest beacon is at x=15, y=3
# Sensor at x=20, y=1: closest beacon is at x=15, y=3"""

beacon_pat = re.compile("Sensor at x=(\d+), y=(\d+): closest beacon is at x=(\d+), y=(\d+)")

sensors = list(map(lambda x:list(map(int,x)),re.findall(beacon_pat, data)))

def manhattan(sensor):
    sx,sy,bx,by = sensor
    return abs(sx-bx)+abs(sy-by)

Y = 2000000

regions = set()

for sx,sy, bx,by in sensors:
    D = manhattan((sx,sy,bx,by))
    x1 = sx - (D-abs(Y-sy))
    x2 = sx + (D-abs(Y-sy))
    regions |= set(range(x1,x2))

print(len(regions))


X_MAX, Y_MAX = 4000000,4000000

offsets_plus, offsets_minus = Counter(), Counter()
for sens in sensors:
    D = manhattan(sens)
    Dplus = sens[0]+sens[1]
    Dminus = sens[0] - sens[1]
    offsets_plus.update([Dplus+D+1,Dplus-D-1])
    offsets_minus.update([Dminus+D+1,Dminus-D-1])

for o1,c1 in offsets_plus.items():
    for o2,c2 in offsets_minus.items():
        if c1>=2 and c2>=2:
            x,y = (o1+o2)//2, (o1-o2)//2
            if 0<=x<=X_MAX and 0<=y<=Y_MAX:
                if all(manhattan(sens[:2]+[x,y])>=manhattan(sens)+1 for sens in sensors):
                    tuning_freq = x*X_MAX+y
                    print(x,y,tuning_freq)

