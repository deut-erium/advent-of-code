import re
with open("input", "r") as f:
    command_pat = "\$ ([\w \n\.\/]+)"
    commands = re.findall(command_pat,f.read())

root = {"/":{}}
paths = root
current_path = []
for command in map(lambda x:x.strip().split("\n"),commands):
    if command[0].startswith("ls"):
        for output in command[1:]:
            typ_siz, name = output.split()
            if typ_siz == "dir":
                paths.setdefault(name,{})
            else:
                paths[name] = int(typ_siz)
    elif command[0].startswith("cd"):
        directory = command[0].split()[1]
        if directory == '..':
            current_path.pop()
        else:
            current_path.append(directory)
            paths = root
            for i in current_path:
                paths = paths[i]

def calculate_sizes(tree):
    if isinstance(tree,int):
        return tree
    if '__total__' not in tree:
        tree_size = 0
        for key, val in tree.items():
            if key!='__total__':
                tree_size += calculate_sizes(val)
        tree['__total__'] = tree_size
    return tree['__total__']

calculate_sizes(root)

def filter_sum(tree, threshold=100000):
    if isinstance(tree, int):
        return 0
    res = 0
    if tree['__total__']<=threshold:
        res += tree['__total__']
    for key, val in tree.items():
        if key!='__total__':
            res += filter_sum(val, threshold)
    return res

print(filter_sum(root))

# PART 2

TOTAL_SPACE = 70000000
MIN_UNUSED = 30000000
MIN_SPACE_TO_FREE = MIN_UNUSED - (TOTAL_SPACE - root['__total__'])

def find_smallest(tree, thresh=MIN_SPACE_TO_FREE, min_sofar=float('inf')):
    if isinstance(tree, int):
        return min_sofar
    if tree['__total__']>thresh:
        min_sofar = min(min_sofar, tree['__total__'])
    for key, val in tree.items():
        if key!='__total__':
            min_sofar = find_smallest(val,thresh,min_sofar)
    return min_sofar

print(find_smallest(root,MIN_SPACE_TO_FREE,float('inf')))



