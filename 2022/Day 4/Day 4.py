assigments = []

with open(r'2022\Day 4\input.txt') as f:
    for line in f:
        pair = line.strip().split(',')
        assigments.append([ tuple(map(int, section.split('-')) )for section in pair]) 
        
completeOverlap = 0
partialOverlap = 0
        
for pair in assigments:
    if pair[0][0] <= pair[1][1] and pair[0][1] >= pair[1][0]:
        partialOverlap += 1
    elif pair[1][0] <= pair[0][1] and pair[1][1] >= pair[0][0]:
        partialOverlap += 1
    
    if pair[0][0] <= pair[1][0] and pair[0][1] >= pair[1][1]:
        completeOverlap += 1
    elif pair[1][0] <= pair[0][0] and pair[1][1] >= pair[0][1]:
        completeOverlap += 1
        
print(completeOverlap, partialOverlap)
