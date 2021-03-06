with open('input.txt') as f:
    data = f.read().strip().split('\n')
    lines = []
    for line_data in data:
        stpt, endpt = line_data.split(' -> ')
        stpt, endpt = stpt.split(','), endpt.split(',')
        stpt,endpt = list(map(int,stpt)), list(map(int,endpt))
        lines.append((stpt,endpt))

def intersection(line1,line2):
    (x1,y1),(x2,y2) = line1
    (X1,Y1),(X2,Y2) = line2
    v1 = (X1-X2)*(y1-y2) - (Y1-Y2)*(x1-x2)
    v2 = (Y2-y2)*(x1-x2) - (X2-x2)*(y1-y2)
    if v2==0 and v1==0:
        return float('inf')
    if v2==0:
        return None
    s = v1/v2
    if 0<=s<=1:
    # return round(s*(X1-X2) + X2,2), round(s*(Y1-Y2) + Y2,2)
        return s*(X1-X2) + X2, s*(Y1-Y2) + Y2
    return None
    
def check_horiz_or_vert(line):
    (x1,y1),(x2,y2) = line
    return x1==x2 or y1==y2


from collections import Counter
# c = Counter()
# for i in range(len(lines)):
#     for j in range(i+1, len(lines)):
#         if check_horiz_or_vert(lines[i]) and check_horiz_or_vert(lines[j]):
#             c[intersection(lines[i],lines[j])]+=1
#             if intersection(lines[i],lines[j])==float('inf'):
#                 print(i,j)

def points_on_line(line):
    (x1,y1),(x2,y2) = line
    if x1==x2:
        if y1>y2:
            y1,y2 = y2,y1
        return ( (x1,y) for y in range(y1,y2+1))
    elif y1==y2:
        if x1>x2:
            x1,x2 = x2,x1
        return ( (x,y1) for x in  range(x1,x2+1))
    elif x1-x2 == y1-y2:
        if x1>x2:
             x1,x2,y1,y2 = x2,x1,y2,y1
        return ( (x1+i,y1+i) for i in range(x2-x1+1))
    elif x1-x2 == y2-y1:
        if x1>x2:
            x1,x2,y1,y2 = x2,x1,y2,y1
        return ( (x1+i,y1-i) for i in range(x2-x1+1))
    return ()

points = Counter()
for l in lines:
    points.update(points_on_line(l))

print(sum(v>1 for v in points.values()))
