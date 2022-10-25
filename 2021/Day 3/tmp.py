with open(r'2021\Day 3\input.txt') as f:
    data = [[int(n) for n in line.strip()] for line in f.readlines()]

import numpy as np

def part1(data):
    arr = np.array(data)
    
    gamma = ''.join([str(int(n > 0.5)) for n in arr.mean(axis=0)])
    epsilon = ''.join([str(int(n < 0.5)) for n in arr.mean(axis=0)])

    part1 = int(gamma, 2) * int(epsilon, 2)
    print(f'part 1: {part1}')


from collections import Counter

def parse_bit_pos(arr, pos):
    
    return Counter(row[pos] for row in arr)

def part2(data):
    L1 = L2 = data
    for i in range(len(data[0])):
        c1, c2 = parse_bit_pos(L1, i), parse_bit_pos(L2, i)
        
        if len(L1) > 1:
            if len(set(c1.values())) == 1:
                L1 = [row for row in L1 if row[i] == 1]
            else:
                L1 = [row for row in L1 if row[i] == max(c1.items(), key=lambda x: x[1])[0]]
        if len(L2) > 1:
            if len(set(c2.values())) == 1:
                L2 = [row for row in L2 if row[i] == 0]
            else:
                L2 = [row for row in L2 if row[i] == min(c2.items(), key=lambda x: x[1])[0]]
            
    o2, co2 = int(''.join([str(n) for n in L1[0]]), 2), int(''.join([str(n) for n in L2[0]]), 2)
    print(L1, L2)
    print(o2 * co2)
    
part2(data)