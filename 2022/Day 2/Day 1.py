strats = []

def decipher_strat(rps):
    if rps in ['A', 'X']:
        return 'R'
    elif rps in ['B', 'Y']:
        return 'P'
    elif rps in ['C', 'Z']:
        return 'S'
    
letter_to_score = { 'R': 1, 'P': 2, 'S': 3 }
rock_paper_scissors_r = { 'R': 'P', 'P': 'S', 'S': 'R' }
rock_paper_scissors = { 'P': 'R', 'S': 'P', 'R': 'S' }

with open(r'2022\Day 2\input.txt') as f:
    for starat in f:
        round = list(starat.strip().split(' '))
        round[0] = decipher_strat(round[0])
        strats.append(round)
        
points1 = 0
points2 = 0
        
for strat in strats:
    if strat[0] == decipher_strat(strat[1]):
        points1 += 3
    elif rock_paper_scissors_r[strat[0]] == decipher_strat(strat[1]):
        points1 += 6
        
    points1 += letter_to_score[decipher_strat(strat[1])]
    
    if strat[1] == 'X':
        points2 += letter_to_score[rock_paper_scissors[strat[0]]]
    elif strat[1] == 'Y':
        points2 += 3
        points2 += letter_to_score[strat[0]]
    else:
        points2 += 6
        points2 += letter_to_score[rock_paper_scissors_r[strat[0]]]
        
print(points1, points2)