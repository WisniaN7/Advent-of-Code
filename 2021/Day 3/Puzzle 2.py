file = open(r'2021\Day 3\input.txt')
firstLine = file.readline().rstrip()
file.close()

binary = []

with open(r'2021\Day 3\input.txt') as f:
    for line in f:
        binary.append(line.rstrip())
        
o2 = binary.copy()

for i in range(len(o2[0])):
    onesCount = 0
    
    for b in o2:
        if b[i] == '1':
            onesCount += 1
            
    if onesCount >= len(o2) * 0.5:
        o2 = list(filter(lambda x: x[i] == '1', o2))
    else:
        o2 = list(filter(lambda x: x[i] == '0', o2))
        
    if len(o2) == 1:
        break
        
co2 = binary.copy()

for i in range(len(co2[0])):
    onesCount = 0
    
    for b in co2:
        if b[i] == '1':
            onesCount += 1
            
    if onesCount < len(co2) * 0.5:
        co2 = list(filter(lambda x: x[i] == '1', co2))
    else:
        co2 = list(filter(lambda x: x[i] == '0', co2))
            
    print(co2)
            
    if len(co2) == 1:
        break
    
    
print(int(o2[0], 2) * int(co2[0], 2))