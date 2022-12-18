def in_chamber_bounds(x):
    return 0 <= x < 7

rockTypes = [
    [(0, 0), (1, 0), (2, 0), (3, 0)],
    [(1, 0), (0, -1), (1, -1), (2, -1), (1, -2)],
    [(2, 0), (2, -1), (0, -2), (1, -2), (2, -2)],
    [(0, 0), (0, -1), (0, -2), (0, -3)],
    [(0, 0), (0, -1), (1, 0), (1, -1)]
]

movements = open(r'2022\Day 17\input.txt').read().strip()
directions = {">": 1, "<": -1}

rocks = set()
height = 0
m = 0

for i in range(2022):
    stopped = False

    if i % 5 == 0:
        pos = [2, height + 3]
    elif i % 5 == 1 or i % 5 == 2:
        pos = [2, height + 5]
    elif i % 5 == 3:
        pos = [2, height + 6]
    elif i % 5 == 4:
        pos = [2, height + 4]

    while True:
        if all(in_chamber_bounds(pos[0] + x + directions[movements[m]]) for x, _ in rockTypes[i % 5]):
            if all((pos[0] + x + directions[movements[m]], pos[1] + y) not in rocks for x, y in rockTypes[i % 5]):
                pos[0] += directions[movements[m]]

        m = (m + 1) % len(movements)
        
        if stopped:
            break
        
        if any((pos[0] + x, pos[1] + y - 1) in rocks for x, y in rockTypes[i % 5]) or pos[1] == 0:
            stopped = True
            break
        
        if not stopped:
            pos[1] -= 1
            
    for x, y in rockTypes[i % 5]:
        rocks.add((pos[0] + x, pos[1] + y))
        
    height = max(pos[1] + 1, height)
    
print(height)
