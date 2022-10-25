file = open(r'2021\Day 3\input.txt')
firstLine = file.readline().rstrip()
file.close()

onesCount = [ 0 for i in range(len(firstLine)) ]
lines = 0

with open(r'2021\Day 3\input.txt') as f:
    for line in f:
        lines += 1
        
        for i, char in enumerate(line):
            if char == '1':
                onesCount[i] += 1

gamma = [ '1' if onesCount[i] > lines >> 1 else '0' for i in range(len(onesCount)) ]
gamma = ''.join(gamma)

epsilon = [ '0' if gamma[i] == '1' else '1' for i in range(len(gamma)) ]
epsilon = ''.join(epsilon)

print(int(gamma, 2) * int(epsilon, 2))