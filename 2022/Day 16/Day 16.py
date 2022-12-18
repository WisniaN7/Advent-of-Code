import re
from collections import defaultdict

def solve(i, time, remaining, elephant):
    ans = solve("AA", 26, remaining, False) if elephant else 0
    
    for j in remaining:
        if (t := time - dist[i][j] - 1) >= 0:
            ans = max(ans, valves[j] * t + solve(j, t, remaining - {j}, elephant))
            
    return ans

valves = {}
dist = defaultdict(lambda: defaultdict(lambda: float('inf')))

with open(r'2022\Day 16\input.txt') as f:
    for line in f:
        ids = re.findall(r'[A-Z][A-Z]', line)
        
        valves[ids[0]] = int(re.search(r'\d+', line)[0])

        for i in ids[1:]:
            dist[ids[0]][i] = 1

for k in valves:
    for i in valves:
        for j in valves:
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
            
print(solve("AA", 30, set(x for x in valves if valves[x] > 0), False))
print(solve("AA", 26, set(x for x in valves if valves[x] > 0), True))