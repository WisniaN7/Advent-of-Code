elves = []

with open(r'2022\Day 1\input.txt') as f:
    calories = []
    
    for calorie in f:
        if calorie != '\n':
            calories.append(int(calorie))
        else:
            elves.append(calories)
            calories = []
            
scores = []
            
for elve in elves:
    scores.append(sum(elve))
        
print(sum(sorted(scores, reverse=True)[:1]))
print(sum(sorted(scores, reverse=True)[:3]))
