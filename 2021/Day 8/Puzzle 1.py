# %%
data = []

with open(r'2021\Day 8\input.txt') as f:
    for line in f:
        data.append(line.strip().split(' | ')) 
        data[-1][0] = data[-1][0].split(' ')
        data[-1][1] = data[-1][1].split(' ')
        
counter = 0
        
for t in data:
    for digit in t[1]: 
        if len(digit) in [2, 3, 4, 7]:
            counter += 1
            
print(counter)
# %%
