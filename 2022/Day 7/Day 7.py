from collections import defaultdict

f = open(r'2022\Day 7\test.txt', 'r')
input = f.readlines()
f.close()

path = []
dirs = {}

for line in input:
    words = line.strip().split(' ')

    if words[1] == 'cd':
        if words[2] == '..':
            path.pop()
        else:
            path.append(words[2])
    elif words[1] == 'ls' or words[0] == 'dir':
        continue
    else:
        for i in range(1, len(path) + 1):
            key = '/'.join(path[:i])
            
            if key not in dirs:
                dirs[key] = 0
            
            dirs[key] += int(words[0])

needToFree = dirs['/'] - 40000000

maxSize = 0
minSize = 1e9

for key, val in dirs.items():
    if val <= 100000:
        maxSize += val

    if val >= needToFree:
        minSize = min(minSize, val)
        
print(maxSize, minSize)