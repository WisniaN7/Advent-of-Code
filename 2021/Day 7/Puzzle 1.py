import numpy as np

data = [int(x) for x in open(r'2021\Day 7\input.txt', 'r').read().split(',')]

median = np.median(data)
print(sum([abs(median - i) for i in data]))