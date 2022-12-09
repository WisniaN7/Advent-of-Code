heightmap = []

with open(r'2022\Day 8\input.txt') as f:
    for line in f:
        heightmap.append(list(map(int, line.strip())))
        
visible = 0
maxVisible = 0

for r in range(len(heightmap)):
    for c in range(len(heightmap[r])):
        tree = heightmap[r][c]
        blocked = [False, False, False, False]
        
        for x in range(c):
            if heightmap[r][x] >= tree:
                blocked[0] = True
                break
            
        for x in range(c + 1, len(heightmap[r])):
            if heightmap[r][x] >= tree:
                blocked[1] = True
                break
            
        for x in range(r):
            if heightmap[x][c] >= tree:
                blocked[2] = True
                break
            
        for x in range(r + 1, len(heightmap)):
            if heightmap[x][c] >= tree:
                blocked[3] = True
                break
        
        if False in blocked:
            visible += 1
        
        view = [0, 0, 0, 0]
        
        for x in range(c - 1, -1, -1):
            view[0] += 1
            
            if heightmap[r][x] >= tree:
                break
            
        for x in range(c + 1, len(heightmap[r])):
            view[1] += 1
            
            if heightmap[r][x] >= tree:
                break
            
        for x in range(r - 1, -1, -1):
            view[2] += 1
            
            if heightmap[x][c] >= tree:
                break
            
        for x in range(r + 1, len(heightmap)):
            view[3] += 1
            
            if heightmap[x][c] >= tree:
                break
            
        maxVisible = max(maxVisible, view[0] * view[1] * view[2] * view[3])
            
print(visible, maxVisible)
