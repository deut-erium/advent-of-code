with open('input.txt','r') as f:
    data = list(map(int,f.read().strip().split()))

seen = set()
TARGET = 2020
for i in data:
    if TARGET-i in seen:
        print(i, TARGET-i, i*(TARGET-i))
    seen.add(i)

seen2 = set()
for i,v1 in enumerate(data):
    for j,v2 in enumerate(data[i+1:],start=i+1):
        if TARGET-v1-v2 in seen2:
            print(v1, v2, TARGET-v1-v2, v1*v2*(TARGET-v1-v2))
        seen2.add(v1)

from itertools import combinations
from math import prod
for k in (2,3):
    seenk = set()
    for vals in combinations(data,k-1):
        if TARGET-sum(vals) in seenk:
            print(*vals, TARGET-sum(vals), prod(vals)*(TARGET-sum(vals)))
        seenk.add(vals[0])


