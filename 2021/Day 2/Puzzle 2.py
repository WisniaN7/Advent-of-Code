import re

position = 0
depth = 0
aim = 0

with open(r'2021\Day 2\input.txt') as f:
    for instriction in f:
        if instriction[0] == 'f':
            x = int(re.findall(r'\d', instriction)[0])
            position += x
            depth += aim * x
        elif instriction[0] == 'd':
            aim += int(re.findall(r'\d', instriction)[0])
        elif instriction[0] == 'u':
            aim -= int(re.findall(r'\d', instriction)[0])
        else:
            raise Exception('Unknown instriction: ' + instriction)
            
print(position * depth)