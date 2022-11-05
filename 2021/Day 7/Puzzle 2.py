import numpy as np

data = [int(x) for x in open(r'2021\Day 7\input.txt', 'r').read().split(',')]

def sum_1_to_n(n): return n * (n + 1) / 2

mean = int(np.mean(data))
print(sum([sum_1_to_n(abs(mean - i)) for i in data]))
