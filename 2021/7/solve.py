
from statistics import median
with open('input.txt') as f:
    data = list(map(int,f.read().strip().split(',')))

best_pos = median(data)

print(sum(map(lambda x: abs(x-best_pos),data)))

min_pos, max_pos = min(data),max(data)
scores = [sum(map(lambda x: abs(x-y)*(abs(x-y)+1)//2,data)) for y in range(min_pos,max_pos)]
print(min(scores))
