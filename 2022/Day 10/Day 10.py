instructions = open(r'2022\Day 10\input.txt').read().split('\n')
cycle = 0
register = 1
signalStrength = 0
CRT = [[' ' for _ in range(40)] for _ in range(6)]

def handleCycle(cycle):
    global register
    global signalStrength
    global CRT
    
    if (cycle + 20) % 40 == 0:
        signalStrength += cycle * register
        
    cycle = cycle - 1
    CRT[cycle // 40][cycle % 40] = ('#' if abs(register - (cycle % 40)) <= 1 else '.')

for i, instruction in enumerate(instructions):
    instruction = instruction.split(' ')
    
    cycle += 1

    if instruction[0][0] == 'n':
        handleCycle(cycle)
    else:
        handleCycle(cycle)
        cycle += 1
        handleCycle(cycle)
        register += int(instruction[1])
            
print(signalStrength)

for line in CRT:
    print(''.join(line))