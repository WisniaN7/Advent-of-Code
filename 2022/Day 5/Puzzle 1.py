import re

stacks = []
endOfStacks = False
instructions = []

with open(r'2022\Day 5\input.txt') as f:
    for line in f:
        if stacks == []:
            for _ in range(0, len(line), 4):
                stacks.append([])
        
        if not endOfStacks:
            for i in range(0, len(line) - 1, 4):
                if line[i + 1 : i + 2] != ' ':
                    stacks[i // 4].append(line[i + 1 : i + 2])
        else:
            instructions.append(tuple(map(int, re.findall(r'\d+', line))))
            
        if line.strip() == '':
            endOfStacks = True
            
            for stack in stacks:
                stack.pop()
                
for stack in stacks:
    stack.reverse()

for instruction in instructions:
    for _ in range(instruction[0]):
        stacks[instruction[2] - 1].append(stacks[instruction[1] - 1].pop())

for stack in stacks:
    print(stack[-1], end='')