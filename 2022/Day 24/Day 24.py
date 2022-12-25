from collections import deque
from operator import add

def has_blizzard(grid, t, i, j):
    global width, height
    
    if (i, j) in ((-1, 0), (height, width - 1)):
        return False
    
    try:
        return grid[(i - t) % height, j] == "v" or grid[(i + t) % height, j] == "^" or grid[i, (j - t) % width] == ">" or grid[i, (j + t) % width] == "<"
    except KeyError:
        return True

def bfs(grid, start, end, t = 0):
    visited = set()
    q = deque([(t, *start)])

    while q:
        p = q.popleft()
        
        if p in visited:
            continue
        
        visited.add(p)

        if p[1:] == end:
            return p[0]

        for d in [(1, 0, 0), (1, -1, 0), (1, 1, 0), (1, 0, -1), (1, 0, 1)]:
            np = tuple(map(add, p, d))
            
            if not has_blizzard(grid, *np):
                q.append(np)

grid = {}
width, height = 0, 0

with open(r'2022\Day 24\input.txt') as f:
    height = len(f.readlines()) - 2
    f.seek(0)
    
    for i, line in enumerate(f.readlines()[1:-1]):
        width = len(line.strip()[1:-1])
        
        for j, char in enumerate(line.strip()[1:-1]):
            grid[(i, j)] = char
            
grid[-1, 0] = grid[height, width - 1] = "."

t1 = bfs(grid, (-1, 0), (height, width - 1))
print(t1)

t2 = bfs(grid, (height, width - 1), (-1, 0), t1)
t3 = bfs(grid, (-1, 0), (height, width - 1), t2)
print(t3)
