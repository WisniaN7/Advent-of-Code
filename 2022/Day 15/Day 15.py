import re

def manhattan_distance(point1, point2):
    distance = 0
    
    for x1, x2 in zip(point1, point2):
        difference = x2 - x1
        absolute_difference = abs(difference)
        distance += absolute_difference

    return distance

def valid(x, y, S):
    for (sx, sy, d) in S:
        dxy = abs(x - sx) + abs(y - sy)
        
        if dxy <= d:
            return False
        
    return True

beacons = set()
sensors = set()

hLimits = [0, 0]
vLimits = [0, 0]

with open(r'2022\Day 15\input.txt') as f:
    for line in f:
        numbers = re.findall(r'-?\d+', line)
        
        v1, h1, v2, h2 = map(int, numbers)
        
        dist = manhattan_distance((v1, h1), (v2, h2))
        sensors.add((v1, h1, dist))
        beacons.add((v2, h2))
        
        hLimits[0] = min(hLimits[0], h1 - dist, h2)
        hLimits[1] = max(hLimits[1], h1 + dist, h2)
        
        vLimits[0] = min(vLimits[0], v1 - dist, v2)
        vLimits[1] = max(vLimits[1], v1 + dist, v2)

blocked = 0
target = int(2e6)

for i in range(hLimits[0], hLimits[1] + 1):
    if not valid(i, target, sensors) and (i, target) not in beacons:
        blocked += 1

print(blocked)

for (sx, sy, d) in sensors:
    for dx in range(d + 2):
        dy = (d + 1) - dx
                
        for signx, signy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            x = sx + (dx * signx)
            y = sy + (dy * signy)
            
            if not (0 <= x <= 4000000 and 0 <= y <= 4000000):
                continue
            
            if valid(x, y, sensors):
                print(x * 4000000 + y)
                exit()