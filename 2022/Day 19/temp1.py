import math
import operator
import re


class _(tuple):
    def put(self, idx, val):
        return _(val if i == idx else x for i, x in enumerate(self))

    def zip_map(self, other, func):
        return _(func(x, y) for x, y in zip(self, other))

    def __add__(self, other):
        return self.zip_map(other, operator.add)

    def __sub__(self, other):
        return self.zip_map(other, operator.sub)

    def __mul__(self, other):
        return _(x * other for x in self)


def blueprints(f):
    ints = re.findall(r"\d+", f.read())
    bps = []
    for offset in range(0, len(ints), 7):
        i, ore, clay, obs_ore, obs_clay, goede_ore, geode_obs = map(int, ints[offset : offset + 7])
        bp = _((ore, 0, 0, 0)), _((clay, 0, 0, 0)), _((obs_ore, obs_clay, 0, 0)), _((goede_ore, 0, geode_obs, 0))
        bps.append((i, bp))
    return bps


def get_time_needed(cost, gain):
    if cost == 0:
        return 0
    if gain == 0:
        return math.inf
    return math.ceil(cost / gain)


def solve(time, blueprint, robots=_((1, 0, 0, 0)), inventory=_((0, 0, 0, 0))):
    ans = inventory[3] + robots[3] * time

    for i in range(3):
        max_useful = time * max([c[i] for c in blueprint]) - robots[i] * time + robots[i]
        if inventory[i] > max_useful:
            inventory = inventory.put(i, max_useful)

    for idx, cost in enumerate(blueprint):
        need_to_earn = cost - inventory
        time_needed = max(need_to_earn.zip_map(robots, get_time_needed))

        if idx < 3 and robots[idx] > max([c[idx] for c in blueprint]):
            continue

        if time_needed >= 0 and time - time_needed - 1 >= 0:
            new_inventory = inventory + robots * (time_needed + 1) - cost
            new_robots = robots + [idx == i for i in range(4)]
            ans = max(ans, solve(time - time_needed - 1, blueprint, new_robots, new_inventory))

    return ans


def p1(f):
    return sum(i * solve(24, blueprint) for i, blueprint in blueprints(f))


def p2(f):
    return max(solve(32, blueprint) for i, blueprint in blueprints(f)[:3])

print(p1(open(r"2022\Day 19\input.txt")))
print(p2(open(r"2022\Day 19\input.txt")))