import re
import time
from collections import deque
from dataclasses import dataclass


@dataclass
class Blueprint:
    def __init__(self):
        self.robots = [1, 0, 0, 0]
        self.resources = [0, 0, 0, 0]
        self.skips = [False, False, False]
        self.time = 0

    @staticmethod
    def copy_blueprint(blueprint):
        new = Blueprint()
        new.robots = list(blueprint.robots)
        new.resources = list(blueprint.resources)
        new.time = blueprint.time
        new.skips = [False, False, False]
        return new

    def __str__(self):
        return str([self.robots, self.resources, self.time])

    def __repr__(self):
        return str([self.robots, self.resources, self.time])


def ceildiv(a, b):
    return -(a // -b)


def get_resources(state, time):
    state = list(state)
    state[0] += time
    for _ in range(time):
        state[5] += state[1]
        state[6] += state[2]
        state[7] += state[3]
        state[8] += state[4]
    return state


def run_blueprint(blueprint, timesteps):
    Q = deque()
    start = [0, 1, 0, 0, 0, 0, 0, 0, 0]
    seen = set()
    Q.append(start)
    n_geodes = 0
    while len(Q) > 0:
        current = Q.popleft()
        if tuple(current) in seen:
            continue
        seen.add(tuple(current))
        # Buy ore
        ore_time = ceildiv((blueprint[1] - current[5]), current[1]) + 1 if current[5] <= blueprint[1] else 1
        ore_needed = max(blueprint[1], blueprint[2], blueprint[3], blueprint[5])
        if current[0] + ore_time < timesteps and current[1] < ore_needed:
            ore = get_resources(current, ore_time)
            ore[1] += 1
            ore[5] -= blueprint[1]
            Q.append(ore)
        clay_time = ceildiv((blueprint[2] - current[5]), current[1]) + 1 if current[5] <= blueprint[2] else 1
        if current[0] + clay_time < timesteps and current[2] < blueprint[4]:
            clay = get_resources(current, clay_time)
            clay[2] += 1
            clay[5] -= blueprint[2]
            Q.append(clay)
        # If clay robot check if we can buy obsidian
        if current[2] > 0:
            if current[5] > blueprint[3] and current[6] > blueprint[4]:
                obsidian_time = 1
            else:
                obsidian_time = max(ceildiv((blueprint[3] - current[5]), current[1]) + 1,
                                    ceildiv((blueprint[4] - current[6]), current[2]) + 1)
            if current[0] + obsidian_time < timesteps and current[3] < blueprint[6]:
                obsidian = get_resources(current, obsidian_time)
                obsidian[3] += 1
                obsidian[5] -= blueprint[3]
                obsidian[6] -= blueprint[4]
                Q.append(obsidian)
        # If obsidian robot check if we can buy geode
        if current[3] > 0:
            if current[5] > blueprint[5] and current[7] > blueprint[6]:
                geode_time = 1
            else:
                geode_time = max(ceildiv((blueprint[5] - current[5]), current[1]) + 1,
                                 ceildiv((blueprint[6] - current[7]), current[3]) + 1)
            if current[0] + geode_time < timesteps:
                geode = get_resources(current, geode_time)
                geode[4] += 1
                geode[5] -= blueprint[5]
                geode[7] -= blueprint[6]
                n_geodes = max(n_geodes, geode[8] + ((timesteps - geode[0]) * geode[4]))
                Q.append(geode)
    return n_geodes


def puzzle1():
    res = 0
    timesteps = 24
    for i, line in enumerate(open('day19.txt').read().splitlines()):
        blueprint = [int(x) for x in re.findall('[0-9]+', line)]
        n_geodes = run_blueprint(blueprint, timesteps)
        res += (i + 1) * n_geodes
    return res


def puzzle2():
    res = 1
    timesteps = 32
    for i, line in enumerate(open('day19.txt').read().splitlines()[:3]):
        blueprint = [int(x) for x in re.findall('[0-9]+', line)]
        n_geodes = run_blueprint(blueprint, timesteps)
        res *= n_geodes
    return res


if __name__ == '__main__':
    start_puzzle1 = int(round(time.time() * 1000))
    res_puzzle1 = puzzle1()
    end_puzzle1 = int(round(time.time() * 1000))
    print("Puzzle 1: " + str(res_puzzle1) + ". Took: " + str((end_puzzle1 - start_puzzle1)))
    start_puzzle2 = int(round(time.time() * 1000))
    res_puzzle2 = puzzle2()
    end_puzzle2 = int(round(time.time() * 1000))
    print("Puzzle 2: " + str(res_puzzle2) + ". Took: " + str((end_puzzle2 - start_puzzle2)))
