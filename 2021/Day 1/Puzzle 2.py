depths = []

with open(r'2021\Day 1\input.txt') as f:
    for depth in f:
        depths.append(int(depth))

sumA = sum(depths[0:3])
sumB = sum(depths[1:4])
increases = 0

for i in range(3, len(depths) - 1):
    if (sumA < sumB):
        increases += 1
    
    sumA = sumB
    sumB = sumB - depths[i - 2] + depths[i + 1]
    
if (sumA < sumB):
    increases += 1
    
print(increases)