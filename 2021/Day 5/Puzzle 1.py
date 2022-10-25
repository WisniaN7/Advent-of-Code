import re

from numpy import diag

diagram = [ [0 for j in range(1000)] for i in range(1000) ]

with open(r'2021\Day 5\input.txt') as f:
    for line in f:
        x1, y1, x2, y2 = re.findall(r'\d+', line)
        delta = (int(x2) - int(x1), int(y2) - int(y1))
        
        if delta[0] == 0 and delta[1] == 0:
            diagram[int(x1)][int(y1)] += 1
        elif delta[0] == 0:
            increment = 1 if delta[1] > 0 else -1 
            
            for y in range(int(y1), int(y2) + increment, increment):
                diagram[y][int(x1)] += 1
        elif delta[1] == 0:
            increment = 1 if delta[0] > 0 else -1 
            
            for x in range(int(x1), int(x2) + increment, increment):
                diagram[int(y1)][x] += 1

counter = 0

for line in diagram:
    for point in line:
        if point > 1:
            counter += 1
            
print(counter)