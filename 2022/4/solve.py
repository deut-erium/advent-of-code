import re
with open("input", "r") as f:
    data = f.read().strip()

ranges = [list(map(int,i)) for i in re.findall("(\d+)-(\d+),(\d+)-(\d+)",data)]

print(sum( (s1<=s2 and e1>=e2) or (s2<=s1 and e2>=e1) for s1,e1,s2,e2 in ranges))

# PART TWO
print(sum(s1<=s2<=e1 or s1<=e2<=e1 or s2<=s1<=e2 or s2<=e1<=e2 for s1,e1,s2,e2 in ranges))
