from collections import deque, namedtuple

def solve(iters = 1, key = 1):
    code = deque((i, int(x) * key) for i, x in enumerate(open(r'2022\Day 20\input.txt').readlines()))
    order = list(code)

    for _ in range(iters):
        for x in order:
            idx = next(i for i, y in enumerate(code) if x[0] == y[0])
            code.rotate(-idx)
            code.popleft()
            code.rotate(-x[1])
            code.appendleft(x)
        
    code.rotate(-next(i for i, x in enumerate(code) if x[1] == 0))
    return code[1000 % len(code)][1] + code[2000 % len(code)][1] + code[3000 % len(code)][1]

print(solve())
print(solve(10, 811589153))