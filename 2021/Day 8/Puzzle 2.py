import string
from pyparsing import alphas

def stringDifference(string: string, chars: string) -> string:
    for c in chars:
        string = string.replace(c, '')
        
    return string

data = []

with open(r'2021\Day 8\input.txt') as f:
    for line in f:
        data.append(line.strip().split(' | ')) 
        data[-1][0] = data[-1][0].split(' ')
        data[-1][1] = data[-1][1].split(' ')
        
sum = 0

for entry in data:
    digits = { i: '' for i in range(10) }
    segments = { alphas[i]: '' for i in range(7) }
    len6 = [] # 0 6 9

    for seq in entry[0]:
        if len(seq) == 2:
            digits[1] = seq
        
        if len(seq) == 3:
            digits[7] = seq
        
        if len(seq) == 4:
            digits[4] = seq
        
        if len(seq) == 6:
            len6.append(seq)
        
        if len(seq) == 7:
            digits[8] = seq
            
    segments['A'] = stringDifference(digits[7], digits[1])

    for digit in len6:
        for c in digits[1]:
            if c not in digit:
                segments['C'] = c
                segments['F'] = stringDifference(digits[1], segments['C'])
                digits[6] = digit
                len6.remove(digits[6])
                break
            
    for digit in len6:
        if len(stringDifference(digits[4], digit)) == 1:
            segments['D'] = stringDifference(digits[4], digit)
            digits[0] = digit
            len6.remove(digits[0])
            break
        
    digits[9] = len6[0]
    segments['E'] = stringDifference(digits[8], digits[9])
    segments['B'] = stringDifference(digits[4], digits[1] + segments['D'])
    segments['G'] = stringDifference(digits[0], digits[7] + segments['B'] + segments['E'])
    
    digits[2] = segments['A'] + segments['C'] + segments['D'] + segments['E'] + segments['G']
    digits[3] = segments['A'] + segments['C'] + segments['D'] + segments['F'] + segments['G']
    digits[5] = segments['A'] + segments['B'] + segments['D'] + segments['F'] + segments['G']
    
    order = 1000
    
    for code in entry[1]:
        for i, digit in digits.items():                
            if ''.join(sorted(code)) == ''.join(sorted(digit)):
                sum += i * order
                order *= 0.1
                break

print(sum)