import json
from functools import cmp_to_key

def clamp(n, smallest, largest): return max(smallest, min(n, largest))

def compare(left, right):
    if type(left) == int and type(right) == int:
        if left < right:
            return -1
        elif left == right:
            return 0
        elif left > right:
            return 1
    elif type(left) == list and type(right) == list:
        for i in range(min(len(left), len(right))):
            cmp = compare(left[i], right[i])
            
            if cmp == -1:
                return -1
            elif cmp == 1:
                return 1
            
        return clamp(len(left) - len(right), -1, 1)
    elif type(left) == int and type(right) == list:
        return compare([left], right)
    else:
        return compare(left, [right])

packets = []

with open(r'2022\Day 13\input.txt') as f:
    index = 1
    indexSum = []
    
    for line in f:
        pair1 = json.loads(line)
        pair2 = json.loads(f.readline())
        packets.append(pair1)
        packets.append(pair2)
        f.readline()

        if compare(pair1, pair2) == -1:
            indexSum.append(index)
            
        index += 1
        
print(sum(indexSum))

packets.append([[2]])
packets.append([[6]])
packets = sorted(packets, key = cmp_to_key(lambda left, right: compare(left, right)))
decoderKey = 1

for i, packet in enumerate(packets):
    if packet == [[2]] or packet == [[6]]:
        decoderKey *= i + 1
        
print(decoderKey)