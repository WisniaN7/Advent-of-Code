#!/usr/bin/python3
import sys
import math
from copy import deepcopy
from collections import defaultdict, deque
infile = sys.argv[1] if len(sys.argv)>1 else r'2022\Day 19\test.txt'
data = open(infile).read().strip()
lines = [x for x in data.split('\n')]

def solve(oreCost, clayCost, obsidianOreCost, obsidianClayCost, geodeOreCost, geodeObsidianCost, time):
    best = 0
    S = (0, 0, 0, 0, 1, 0, 0, 0, time)
    Q = deque([S])
    SEEN = set()
    
    while Q:
        state = Q.popleft()
        #print(state)
        ore, clay, obsidian, geode, robotOre, robotClay, robotObsidian, robotGeode, t = state

        best = max(best, geode)
        
        if t == 0:
            continue

        Core = max([oreCost, clayCost, obsidianOreCost, geodeOreCost])
        
        if robotOre >= Core:
            robotOre = Core
        
        if robotClay >= obsidianClayCost:
            robotClay = obsidianClayCost
        
        if robotObsidian >= geodeObsidianCost:
            robotObsidian = geodeObsidianCost
        
        if ore >= t * Core-robotOre * (t - 1):
            ore = t * Core - robotOre * (t - 1)
        
        if clay >= t * obsidianClayCost - robotClay * (t - 1):
            clay = t * obsidianClayCost  -  robotClay * (t - 1)
        
        if obsidian >= t * geodeObsidianCost - robotObsidian * (t - 1):
            obsidian = t * geodeObsidianCost - robotObsidian * (t - 1)

        state = (ore, clay, obsidian, geode, robotOre, robotClay, robotObsidian, robotGeode, t)

        if state in SEEN:
            continue
        
        SEEN.add(state)

        if len(SEEN) % 1000000 == 0:
            print(t, best, len(SEEN))
        
        assert ore >= 0 and clay >= 0 and obsidian >= 0 and geode >= 0, state
        
        Q.append((ore + robotOre, clay + robotClay, obsidian + robotObsidian, geode + robotGeode, robotOre, robotClay, robotObsidian, robotGeode, t - 1))
        
        if ore >= oreCost: #
            Q.append((ore - oreCost + robotOre, clay + robotClay, obsidian + robotObsidian, geode + robotGeode, robotOre + 1, robotClay, robotObsidian, robotGeode, t - 1))
        
        if ore >= clayCost:
            Q.append((ore - clayCost + robotOre, clay + robotClay, obsidian + robotObsidian, geode + robotGeode, robotOre, robotClay + 1, robotObsidian, robotGeode, t - 1))
        
        if ore >= obsidianOreCost and clay >= obsidianClayCost:
            Q.append((ore - obsidianOreCost + robotOre, clay - obsidianClayCost + robotClay, obsidian + robotObsidian, geode + robotGeode, robotOre, robotClay, robotObsidian + 1, robotGeode, t - 1))
        
        if ore >= geodeOreCost and obsidian >= geodeObsidianCost:
            Q.append((ore - geodeOreCost + robotOre, clay + robotClay, obsidian - geodeObsidianCost + robotObsidian, geode + robotGeode, robotOre, robotClay, robotObsidian, robotGeode + 1, t - 1))
    
    return best


p1 = 0
p2 = 1

for i, line in enumerate(lines):
    words = line.split()
    id_ = int(words[1][:-1])
    ore_cost = int(words[6])
    clay_cost = int(words[12])
    obsidian_cost_ore, obsidian_cost_clay = int(words[18]), int(words[21])
    geode_cost_ore, geode_cost_clay = int(words[27]), int(words[30])
    s1 = solve(ore_cost, clay_cost, obsidian_cost_ore, obsidian_cost_clay, geode_cost_ore, geode_cost_clay, 24)
    p1 += id_ * s1
    
    if i < 3:
        s2 = solve(ore_cost, clay_cost, obsidian_cost_ore, obsidian_cost_clay, geode_cost_ore, geode_cost_clay, 32)
        p2 *= s2
        
print(p1)
print(p2)