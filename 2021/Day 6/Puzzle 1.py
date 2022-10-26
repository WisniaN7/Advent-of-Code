lanterfish = []

with open(r'2021\Day 6\input.txt') as f:
    lanterfish = list(map(int, f.read().split(',')))
    
for i in range(80):
    for i in range(len(lanterfish)):
        if lanterfish[i] == 0:
            lanterfish[i] = 6
            lanterfish.append(8)
        else:
            lanterfish[i] -= 1
            
print(len(lanterfish))