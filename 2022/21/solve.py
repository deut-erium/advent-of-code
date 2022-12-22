import ast
with open("input") as f:
    data = f.read().strip()

# data = """root: pppw + sjmn
# dbpl: 5
# cczh: sllz + lgvd
# zczc: 2
# ptdq: humn - dvpt
# dvpt: 3
# lfqf: 4
# ljgn: 2
# sjmn: drzm * dbpl
# sllz: 4
# pppw: cczh / lfqf
# lgvd: ljgn * ptdq
# drzm: hmdt - zczc
# hmdt: 32"""

data = data.replace("/", "//")

# PART 1
# procedures = {}
# for line in data.split("\n"):
#     proc_name, expression = line.split(": ")
#     procedures[proc_name] = compile(ast.parse(expression,mode="eval"),filename="",mode="eval")

# VALUES = {}

# def shout(name):
#     if name in VALUES:
#         return VALUES[name]
#     proc = procedures[name]
#     VALUES[name] = eval(proc,{i:shout(i) for i in proc.co_names},{})
#     return VALUES[name]

# print(shout('root'))

procedures = {}
for line in data.split("\n"):
    proc_name, expression = line.split(": ")
    if proc_name == 'humn':
        continue
    if proc_name == 'root':
        expression = expression.replace("+","-").replace("*","-").replace("//","-")
    procedures[proc_name] = compile(ast.parse(expression,mode="eval"),filename="",mode="eval")


def eval_humn(val):
    VALUES = {"humn":val}
    def shout(name):
        if name in VALUES:
            return VALUES[name]
        proc = procedures[name]
        VALUES[name] = eval(proc,{i:shout(i) for i in proc.co_names},{})
        return VALUES[name]
    return shout("root")

lo, hi = -2**63, 2**63
sign_lo = (-1)**(eval_humn(lo)<0)
while lo<=hi:
    mid = (lo+hi)//2
    if eval_humn(mid)==0:
        print(mid)
        break
    if sign_lo*eval_humn(mid)<0:
        hi = mid
    else:
        lo = mid
