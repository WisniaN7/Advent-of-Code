# Could be optimized a lot, but don't have time for that

from operator import add

def add_tuple(a, b):
    return tuple(x + y for x, y in zip(a, b))

elves = {}
counter = 0

with open(r'2022\Day 23\input.txt') as f:
    for i, line in enumerate(f):
        for j, c in enumerate(line):
            if c == '#':
                elves[counter] = (j, i)
                counter += 1
                
orth = [(0, 1), (0, -1), (-1, 0), (1, 0)]
diag = [(-1, 1), (1, 1), (1, -1), (-1, -1)]

dirs = [ ((-1, -1), (0, -1), (1, -1)), ((-1, 1), (0, 1), (1, 1)), ((-1, -1), (-1, 0), (-1, 1)), ((1, 1), (1, 0), (1, -1)) ]

for r in range(10):
    elvesPropositions = {}
    
    for elf, pos in elves.items():
        if all(list(tuple(map(add, pos, (orth + diag)[i])) for i in range(8))[j] not in elves.values() for j in range(8)):
            elvesPropositions[elf] = pos
            continue
        
        for i in range(4):
            if all(list(tuple(map(add, pos, dirs[i][j])) for j in range(3))[k] not in elves.values() for k in range(3)):
                elvesPropositions[elf] = tuple(map(add, pos, dirs[i][1]))
                break
            
    for k1, v1 in elvesPropositions.items():
        if any(k1 != k2 and v1 == v2 for k2, v2 in elvesPropositions.items()):
            continue
            
        elves[k1] = v1

    dirs.append(dirs.pop(0))

minCoords = (min(elves.values(), key=lambda x: x[0])[0], min(elves.values(), key=lambda x: x[1])[1])
maxCoords = (max(elves.values(), key=lambda x: x[0])[0], max(elves.values(), key=lambda x: x[1])[1])
print((((maxCoords[0] - minCoords[0]) + 1) * ((maxCoords[1] - minCoords[1]) + 1)) - len(elves))

for r in range(10000):
    elvesPropositions = {}
    changed = False
    
    for elf, pos in elves.items():
        if all(list(tuple(map(add, pos, (orth + diag)[i])) for i in range(8))[j] not in elves.values() for j in range(8)):
            elvesPropositions[elf] = pos
            continue
        
        for i in range(4):
            if all(list(tuple(map(add, pos, dirs[i][j])) for j in range(3))[k] not in elves.values() for k in range(3)):
                elvesPropositions[elf] = tuple(map(add, pos, dirs[i][1]))
                changed = True
                break
            
    if not changed:
        print(r + 11)
        break
            
    for k1, v1 in elvesPropositions.items():
        if any(k1 != k2 and v1 == v2 for k2, v2 in elvesPropositions.items()):
            continue
            
        elves[k1] = v1

    dirs.append(dirs.pop(0))