import sys
import re
from functools import reduce
import operator as op

PATTERN = re.compile("""Monkey (?P<monkey_id>\d+):
  Starting items: (?P<items>\d+(, \d+)*)
  Operation: new = (?P<op>.+)
  Test: divisible by (?P<div_test>\d+)
    If true: throw to monkey (?P<true_monkey>\d+)
    If false: throw to monkey (?P<false_monkey>\d+)
""")

MONKEYS = []

class Monkey():
    def __init__(self, monkey_id='', items=(), op='', div_test='', true_monkey='', false_monkey=''):
        self.id = int(monkey_id)
        self.items = list(map(int, items.split(', ')))
        self.op = eval(f"lambda old: {op}")  # hack
        self.div_test = int(div_test)
        self.true_monkey = int(true_monkey)
        self.false_monkey = int(false_monkey)
        self.count = 0
        return

    def step(self):
        self.count += len(self.items)
        for _ in range(len(self.items)):
            item = self.items.pop(0)
            item = self.op(item) // 3
            if item % self.div_test == 0:
                MONKEYS[self.true_monkey].items.append(item)
            else:
                MONKEYS[self.false_monkey].items.append(item)
        return

done = False
while not done:
    x = "".join(next(sys.stdin) for _ in range(6))
    match = PATTERN.match(x)
    groups = match.groupdict()
    m = Monkey(**groups)
    MONKEYS.append(m)
    try:
        next(sys.stdin)
    except StopIteration:
        done = True

for _ in range(20):
    for m in MONKEYS:
        m.step()
#   for m in MONKEYS:
#       print(f"Monkey {m.id}: {', '.join(map(str, m.items))}")
#   print()

print(reduce(op.mul, sorted((m.count for m in MONKEYS), reverse=True)[:2]))
