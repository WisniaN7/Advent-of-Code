def getArea(x: int, y: int, heightMap: list) -> list:
    if (x, y) == (0, 0):
        return [heightMap[x + 1][y], heightMap[x][y + 1]]
    elif (x, y) == (len(heightMap) - 1, len(heightMap[0]) - 1):
        return [heightMap[x-1][y], heightMap[x - 1][y - 1]]
    elif (x, y) == (0, len(heightMap[0]) - 1):
        return [heightMap[x][y - 1], heightMap[x + 1][y]]
    elif y == len(heightMap[0]) - 1:
        return [heightMap[x - 1][y], heightMap[x][y - 1], heightMap[x + 1][y]]
    elif (x, y) == (len(heightMap) - 1, 0):
        return [heightMap[x - 1][y], heightMap[x][y + 1]]
    elif x == len(heightMap) - 1:
        return [heightMap[x - 1][y], heightMap[x][y - 1], heightMap[x][y + 1]]
    elif x == 0:
        return [heightMap[x][y - 1], heightMap[x + 1][y], heightMap[x][y + 1]]
    elif y == 0:
        return [heightMap[x - 1][y], heightMap[x + 1][y], heightMap[x][y + 1]]

    return [heightMap[x - 1][y], heightMap[x][y - 1], heightMap[x + 1][y], heightMap[x][y + 1]]

heightMap = []

with open(r'2021\Day 9\input.txt') as f:
    for line in f:
        heightMap.append(list(line.strip()))

riskLevel = 0

for x in range(len(heightMap)):
    for y in range(len(heightMap[0])):
        height = heightMap[x][y]
        area = getArea(x, y, heightMap)
        
        if height < min(area):
            riskLevel += 1 + int(height)
            
print(riskLevel)