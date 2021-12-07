with open('input.txt') as f:
    fishes = list(map(int,f.read().strip().split(',')))

fishpool = [0 for _ in range(9)]
for f in fishes:
    fishpool[f]+=1


for day in range(256):
    first = fishpool[0]
    newpool = fishpool[1:]+[first]
    newpool[-3]+=first
    fishpool = newpool

print(sum(fishpool))
