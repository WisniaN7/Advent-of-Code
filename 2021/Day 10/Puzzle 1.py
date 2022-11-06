import queue

points = { ')': 3, ']': 57, '}': 1197, '>': 25137 }
score = 0

openBrackets = '([{<'
closeBrackets = ')]}>'

with open(r'2021\Day 10\input.txt') as f:
    for line in f:
        lifo = []
        
        for c in line.strip():
            if c in openBrackets:
                lifo.append(c)
            elif closeBrackets.index(c) == openBrackets.index(lifo[-1]):
                lifo.pop()
            else:
                score += points[c]
                break
                
print(score)
