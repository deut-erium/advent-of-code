from functools import cmp_to_key
import ast
with open("input", "r") as f:
    data = [i.split("\n") for i in f.read().strip().split("\n\n")]

WHITELIST = (ast.Expression, ast.List, ast.Load, ast.Constant)
def safe_eval(expr):
    tree = ast.parse(expr,mode='eval')
    if all(isinstance(node, WHITELIST) for node in ast.walk(tree)):
        return eval(compile(tree, filename='', mode='eval'))

pairs = [(safe_eval(i[0]),eval(i[1])) for i in  data]

def compare(left, right):
    if isinstance(left, int) and isinstance(right, int):
        return left-right
    if isinstance(left, list) and isinstance(right, list):
        for a,b in zip(left,right):
            comp = compare(a,b)
            if comp:
                return comp
        return len(left)-len(right)
    if isinstance(left, (int,float)):
        return compare([left], right)
    return compare(left, [right])

sum_ind = 0
for i,(left,right) in enumerate(pairs):
    if compare(left, right)<0:
        sum_ind += i+1

dividers = [[[2]],[[6]]]
packets = sorted([i for j in pairs for i in j]+dividers, key=cmp_to_key(compare))

d0 = packets.index(dividers[0])+1
d1 = packets.index(dividers[1])+1
print(d0*d1)


