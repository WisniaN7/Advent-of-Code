import re

class Moneky:
    def __init__(self, id, items, operation, test, monkeyT, monkeyF) -> None:
        self.id = id
        self.items = items
        self.operation = operation
        self.test = test
        self.monkeys = (monkeyT, monkeyF)
        self.inspectedItems = 0
        
    def throw(self, item):
        if item % self.test == 0:
            monkeys[self.monkeys[0]].items.append(item)
        else:
            monkeys[self.monkeys[1]].items.append(item)

    def inspect(self, old):
        old = int(old)
        new = eval(self.operation)
        self.inspectedItems += 1
        return new # // 3
    
    def cleanup(self):
        self.items = []
            
monkeys = []
            
with open(r'2022\Day 11\input.txt') as f:
    for line in f:
        id = int(line[7])
        line = f.readline().strip()
        items = list(re.findall(r'\d+', line))
        line = f.readline().strip()
        operation = line[17:]
        line = f.readline().strip()
        test = int(line[18:])
        line = f.readline().strip()
        monkeyT = int(line[24:])
        line = f.readline().strip()
        monkeyF = int(line[25:])
        line = f.readline().strip()
        monkeys.append(Moneky(id, items, operation, test, monkeyT, monkeyF))
        
mod = 1
        
for monkey in monkeys:
    mod *= monkey.test

for round in range(10000):
    for monkey in monkeys:
        for item in range(len(monkey.items)):
            monkey.items[item] = monkey.inspect(monkey.items[item])
            monkey.items[item] %= mod
            monkey.throw(monkey.items[item])
            
        monkey.cleanup()
        
inspectedItems = []

for monkey in monkeys:
    inspectedItems.append(monkey.inspectedItems)
    
print(sorted(inspectedItems, reverse=True)[0] * sorted(inspectedItems, reverse=True)[1])