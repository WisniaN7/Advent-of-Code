fuel = 0
SNAFU = { '2': 2, '1': 1, '0': 0, '-': -1, '=': -2 }
SNAFU_R = { 2: '2', 1: '1', 0: '0', -1: '-', -2: '=' }

with open(r'2022\Day 25\input.txt') as f:
    for line in f:
        for pow, c in enumerate(reversed(line.strip())):
            fuel += SNAFU[c] * (5 ** pow)
            
snafu = ''
        
while fuel > 0:
    fuel, digit = divmod(fuel, 5)
    
    if digit > 2:
        digit -= 5
        fuel += 1
        
    snafu += SNAFU_R[digit]
    
print(snafu[::-1])