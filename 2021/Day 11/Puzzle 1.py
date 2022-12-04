import numpy as np

def flash(index : int, o, flashed : list) -> None:
    flashed[index] = True
    topRow = index - 10 < 0
    leftCol = (index - 1) // 10 != index // 10
    botRow = index + 10 >= 100
    rightCol = (index + 1) // 10 != index // 10
    
    if not topRow:
        if not leftCol:
            o[index - 11] += 1

            if o[index - 11] > 9 and not flashed[index - 11]:
                flash(index - 11, o, flashed)
            
        o[index - 10] += 1

        if o[index - 10] > 9 and not flashed[index - 10]:
            flash(index - 10, o, flashed)
        
        if not rightCol:
            o[index - 9] += 1

            if o[index - 9] > 9 and not flashed[index - 9]:
                flash(index - 9, o, flashed)
            
    if not leftCol:
        o[index - 1] += 1

        if o[index - 1] > 9 and not flashed[index - 1]:
            flash(index - 1, o, flashed)
            
    if not rightCol:
        o[index + 1] += 1
    
    if not botRow:
        if not leftCol:
            o[index + 9] += 1
            
        o[index + 10] += 1
        
        if not rightCol:
            o[index + 11] += 1

octopodes = np.zeros(100)

with open(r'2021\Day 11\test.txt') as f:    
    i = 0
    
    for line in f:
        for c in line.strip():
            octopodes[i] = int(c)
            i += 1

flashes = 0

for i in range(10):
    print(octopodes[i * 10 : (i * 10) + 10])

for day in range(100):
    flashed = np.array([ False for _ in range(100) ])
    octopodes += 1
    
    for i, o in enumerate(octopodes):
        if o > 9:
            flash(i, octopodes, flashed)
            
    for i, o in enumerate(octopodes):
        if o > 9:
            flashes += 1
            octopodes[i] = 0
            
    if day < 9 or day % 10 == 9:
        print('Day:', day + 1)
    
        for i in range(10):
            print(octopodes[i * 10 : (i * 10) + 10])
        
        print()
            
print(flashes)