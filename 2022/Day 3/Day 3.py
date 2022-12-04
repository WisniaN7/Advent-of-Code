
rucksacks = []
groups = []

with open(r'2022\Day 3\input.txt') as f:
    group = []
    
    for i, items in enumerate(f):
        rucksacks.append(items.strip())
        group.append(items.strip())
        
        if i % 3 == 2:
            groups.append(group)
            group = []

priority = 0
        
for items in rucksacks:
    items = (items[:len(items) // 2], items[len(items) // 2:])

    for letter in items[0]:
        if letter in items[1]:
            if letter.isupper():
                priority += ord(letter.lower()) - 96 + 26
            else:
                priority += ord(letter) - 96

            break
        
print(priority)
priority = 0

for group in groups:
    for letter in group[0]:
        if letter in group[1] and letter in group[2]:
            if letter.isupper():
                priority += ord(letter.lower()) - 96 + 26
            else:
                priority += ord(letter) - 96

            break

        
print(priority)