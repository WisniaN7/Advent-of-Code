cave = set()
hLimits = [500, 500]
vLimits = [0, 0]

with open(r'2022\Day 14\input.txt') as f:
    for line in f:
        line = line.strip().split(r'->')
        
        for i in range(len(line) - 1):
            h1, v1 = tuple(map(int, line[i].split(r',')))
            h2, v2 = tuple(map(int, line[i + 1].split(r',')))
            
            if h1 == h2:
                start = min(v1, v2)
                end = max(v1, v2)
                
                for v in range(start, end + 1):
                    cave.add((h1, v))
            elif v1 == v2:
                start = min(h1, h2)
                end = max(h1, h2)
                
                for h in range(start, end + 1):
                    cave.add((h, v1))

            vLimits = [min(vLimits[0], v1, v2), max(vLimits[1], v1, v2)]
            hLimits = [min(hLimits[0], h1, h2), max(hLimits[1], h1, h2)]
            
grainsfOfSand = 0
simulating = True

while simulating:
    sand = (500, 0)
    
    while True:
        if sand[0] == vLimits[0] or sand[0] == vLimits[1] or sand[1] == hLimits[1] or sand[1] == hLimits[0]:
            simulating = False
            break
        elif (sand[0], sand[1] + 1) not in cave:
            sand = (sand[0], sand[1] + 1)
        elif (sand[0] - 1, sand[1] + 1) not in cave:
            sand = (sand[0] - 1, sand[1] + 1)
        elif (sand[0] + 1, sand[1] + 1) not in cave:
            sand = (sand[0] + 1, sand[1] + 1)
        else:
            cave.add(sand)
            grainsfOfSand += 1
            break

print(grainsfOfSand)

grainsfOfSand = 0
simulating = True
floor = 2 + max(vLimits)

while simulating:
    sand = (500, 0)
    firstIter = True
    
    while True:
        if (sand[0], sand[1] + 1) not in cave and sand[1] + 1 != floor:
            sand = (sand[0], sand[1] + 1)
        elif (sand[0] - 1, sand[1] + 1) not in cave and sand[1] + 1 != floor:
            sand = (sand[0] - 1, sand[1] + 1)
        elif (sand[0] + 1, sand[1] + 1) not in cave and sand[1] + 1 != floor:
            sand = (sand[0] + 1, sand[1] + 1)
        else:
            cave.add(sand)
            grainsfOfSand += 1
            break
        
    if sand == (500, 0):
        simulating = False

print(grainsfOfSand)