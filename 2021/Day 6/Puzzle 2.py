lanterfish = [0 for i in range(9)]

with open(r'2021\Day 6\input.txt') as f:
    initialFish = list(map(int, f.read().split(',')))
    
    for fish in initialFish:
        lanterfish[fish] += 1
        

for day in range(256):
    newFish = lanterfish[0]
    
    for i in range(1, len(lanterfish)):
        lanterfish[i - 1] = lanterfish[i]
        
    lanterfish[-1] = newFish
    lanterfish[6] += newFish

print(sum(lanterfish))