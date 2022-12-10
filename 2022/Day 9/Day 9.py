import math

directinos = {'U': (0, 1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}

def simlateRope(steps, length):
    positions = set()
    knots = [(0, 0)] * length
    prevKnots = [(0, 0)] * length

    for step in steps:
        dx, dy = directinos[step[0]]
        
        for _ in range(int(step[1:])):
            knots[0] = (knots[0][0] + dx, knots[0][1] + dy)
                
            for i in range(1, length):
                px, py = knots[i - 1]
                kx, ky = knots[i]
                
                while max(abs(kx - px), abs(ky - py)) > 1:
                    if abs(kx - px) > 0:
                        kx += 1 if px > kx else -1
                        
                    if abs(ky - py) > 0:
                        ky += 1 if py > ky else -1
                        
                knots[i] = kx, ky
                
            positions.add(knots[-1])
        
    return len(positions)

steps = open(r'2022\Day 9\input.txt').read().split('\n')

print(simlateRope(steps, 2))
print(simlateRope(steps, 10))