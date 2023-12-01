import re

def fitness(buyOrder = ['None' for _ in range(24)], blueprint = { 'ore' : 1, 'clay' : 1, 'obsidian' : 1, 'geode' : 1 }):
    resources = {'ore': 0, 'clay': 0, 'obsidian': 0, 'geode': 0}
    robots = {'ore': 1, 'clay': 0, 'obsidian': 0, 'geode': 0}
    geodesMined = 0

    for i in range(24):
        resources = dict(map(lambda x: (x[0], x[1] + robots[x[0]]), resources.items()))
        
        if buyOrder[i] == 'None':
            continue
        elif buyOrder[i] == 'ore':
            if blueprint['ore'] <= resources['ore']:
                robots['ore'] += 1
        elif buyOrder[i] == 'clay':
            if blueprint['clay'] <= resources['clay']:
                robots['clay'] += 1
        elif buyOrder[i] == 'obsidian':
            if blueprint['obsidian'] <= resources['obsidian']:
                robots['obsidian'] += 1
        elif buyOrder[i] == 'geode':
            if blueprint['geode'] <= resources['geode']:
                robots['geode'] += 1
                
    return geodesMined * 5

blueprints = []

with open(r'2022\Day 19\test.txt') as f:
    for line in f:
        blueprint = {}
        costs = re.findall(r'\d+', line)

        blueprint['None'] = 0
        blueprint['ore'] = int(costs[1])
        blueprint['clay'] = int(costs[2])
        blueprint['obsidian'] = (int(costs[3]), int(costs[4]))
        blueprint['geode'] = (int(costs[5]), int(costs[6]))
        
        blueprints.append(blueprint)    

