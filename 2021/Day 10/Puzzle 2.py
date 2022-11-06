openBrackets = '([{<'
closeBrackets = ')]}>'

incompleteLines = []
notClosedBrackets = []

with open(r'2021\Day 10\input.txt') as f:
    for line in f:
        incompleteLines.append(line.strip())
        notClosedBrackets.append(True)
        lifo = []
        
        for c in line.strip():
            if c in openBrackets:
                lifo.append(c)
            elif closeBrackets.index(c) == openBrackets.index(lifo[-1]):
                lifo.pop()
            else:
                notClosedBrackets[-1] = False
                incompleteLines.pop()
                break
            
        if notClosedBrackets[-1]:
            notClosedBrackets[-1] = lifo
        else:
            notClosedBrackets.pop()
            
scores = []
            
for line in notClosedBrackets:
    score = 0
    
    for bracket in reversed(line):
        for c in openBrackets:
            if bracket == c:
                score *= 5
                score += closeBrackets.index(closeBrackets[openBrackets.index(bracket)]) + 1
                break
    
    scores.append(score)
    
print(sorted(scores)[len(scores) // 2])