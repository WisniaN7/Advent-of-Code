import copy
from sympy import solve, symbols, Eq, Symbol 

def substitute_vals(monkeys, key = 'root'):
    if type(monkeys[key]) in [float, Symbol]:
        return monkeys[key]
    
    for i, k in enumerate(monkeys[key][1:]):
        monkeys[key][i + 1] = substitute_vals(monkeys, k)
        
    if monkeys[key][0] == '+':
        monkeys[key] = monkeys[key][1] + monkeys[key][2]
    elif monkeys[key][0] == '*':
        monkeys[key] = monkeys[key][1] * monkeys[key][2]
    elif monkeys[key][0] == '-':
        monkeys[key] = monkeys[key][1] - monkeys[key][2]
    elif monkeys[key][0] == '/':
        monkeys[key] = monkeys[key][1] / monkeys[key][2]
    
    return monkeys[key]

monkeys1 = {}

with open(r'2022\Day 21\input.txt') as f:
    for line in f:
        line = line.strip()
        
        try:
            monkeys1[line[:4]] = float(line[6:])
        except:
            monkeys1[line[:4]] = [line[11], line[6:10], line[13:]]
            
monkeys2 = copy.deepcopy(monkeys1)
monkeys2['humn'] = symbols('x')
monkeys2['root'][0] = '='

substitute_vals(monkeys1)
substitute_vals(monkeys2)
print(monkeys1['root'])
print(solve(Eq(monkeys2['root'][1], monkeys2['root'][2])))