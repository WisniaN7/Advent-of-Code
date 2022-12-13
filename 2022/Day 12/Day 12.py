def bfs(part):
    queue = []
    
    for r in range(rows):
        for c in range(cols):
            if (part == 1 and charmap[r][c] == 'S') or (part == 2 and heightmap[r][c] == 1):
                queue.append(((r,c), 0))

    visited = set()
    
    while queue:
        (r,c), steps = queue.pop(0)
        
        if (r,c) in visited:
            continue
        
        visited.add((r,c))
        
        if charmap[r][c] == 'E':
            return steps
        
        for dr,dc in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            nr = r + dr
            nc = c + dc
            
            if 0 <= nr < rows and 0 <= nc < cols and heightmap[nr][nc] <= 1 + heightmap[r][c]:
                queue.append(((nr,nc), steps + 1))

charmap = []

with open(r'2022\Day 12\input.txt') as f:
    for line in f:
        charmap.append(list(line.strip()))

rows = len(charmap)
cols = len(charmap[0])

heightmap = [[0 for _ in range(cols)] for _ in range(rows)]

for r in range(rows):
    for c in range(cols):
        if charmap[r][c] == 'S':
            heightmap[r][c] = 1
        elif charmap[r][c] == 'E':
            heightmap[r][c] = 26
        else:
            heightmap[r][c] = ord(charmap[r][c]) - ord('a') + 1
            
print(bfs(1))
print(bfs(2))