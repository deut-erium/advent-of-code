import re
import ast
from collections import deque

with open("input", "r") as f:
    monkey_data = f.read().strip().split("\n\n")

MONKEY_PATTERN = re.compile(r"""Monkey (\d+):
  Starting items: (.*)
  Operation: new = (.*)
  Test: divisible by (\d+)
    If true: throw to monkey (\d+)
    If false: throw to monkey (\d+)""")
WHITELIST = (ast.Expression, ast.Call, ast.BinOp, ast.Name, ast.UnaryOp, ast.unaryop, ast.Num, ast.Load, ast.operator)

NUM_ROUNDS = 10000
MAX_MOD = 1

class Monkey:
    def __init__(self, state_str):
        self.num_inspected = 0
        self.parse_state(state_str)

    def parse_state(self, state_string):
        name, items, expr, divisibility, true_jump, false_jump = re.search(MONKEY_PATTERN, state_string).groups()
        self.name = name
        self.items = deque(list(map(int,items.split(", "))))
        tree = ast.parse(expr,mode='eval')
        if all(isinstance(node, WHITELIST) for node in ast.walk(tree)):
            self.expr = compile(tree, filename='', mode='eval')
        self.true = true_jump
        self.false = false_jump
        self.divisibility = int(divisibility)

    def __repr__(self):
        return f"{self.name}, {self.items}"

    def update(self, old):
        return eval(self.expr, {"old":old})

    def process(self):
        while self.items:
            current = self.items.popleft()
            new_val = self.update(current)//1 # 3 for PART 1
            new_val = new_val%MAX_MOD
            self.num_inspected+=1
            if new_val%self.divisibility==0:
                yield new_val, self.true
            else:
                yield new_val, self.false

monkeys = {}
for monkey_str in monkey_data:
    monkey = Monkey(monkey_str)
    monkeys[monkey.name] = monkey
    MAX_MOD *= monkey.divisibility

for round in range(NUM_ROUNDS):
    for i in range(len(monkeys)):
        for new_val, monkey_num in monkeys[str(i)].process():
            monkeys[monkey_num].items.append(new_val)

num_inspected = sorted([i.num_inspected for i in monkeys.values()])
print(num_inspected[-1]*num_inspected[-2])



