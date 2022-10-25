from numpy import Infinity


increases = 0
previousDepth = Infinity

with open(r'2021\Day 1\input.txt') as f:
    for depth in f:
        if (int(depth) > previousDepth):
            increases += 1
            
        previousDepth = int(depth)

print(increases)