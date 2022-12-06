datastream = ''

with open(r'2022\Day 6\input.txt') as f:
    datastream = f.read().strip()
    
    
for i in range(0, len(datastream)):
    buffer = set(datastream[i:i+4])
    
    if len(buffer) == 4:
        print(i + 4)
        break
    
for i in range(0, len(datastream)):
    buffer = set(datastream[i:i+14])
    
    if len(buffer) == 14:
        print(i + 14)
        break