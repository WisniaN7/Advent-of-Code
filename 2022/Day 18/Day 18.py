from operator import add

coordinates = set()

with open(r'2022\Day 18\input.txt') as f:
    for line in f:
        coordinates.add(tuple(map(int, line.strip().split(','))))
        
        

notCovered = 0

for coord in coordinates:
    notCovered += 6
    
    for neighbor in [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]:
        if tuple(map(add, coord, neighbor)) in coordinates:
            notCovered -= 1

print(notCovered)



notCovered = 0

min_coords = tuple(min(x) - 1 for x in zip(*coordinates))
max_coords = tuple(max(x) + 1 for x in zip(*coordinates))

visited = set()
q = [min_coords]

while q:
    coord = q.pop()

    if coord in visited:
        continue
    
    visited.add(coord)
    
    for neighbor in [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]:
        n = tuple(map(add, coord, neighbor))
        
        if all(a <= b <= c for a, b, c in zip(min_coords, n, max_coords)):
            if n in coordinates:
                notCovered += 1
            else:
                q.append(n)
                
print(notCovered)
