import collections
import time
import re

grid = {
    'e': (1, 0),
    'se': (0, -1),
    'sw': (-1, -1),
    'w': (-1, 0),
    'nw': (0, 1),
    'ne': (1, 1),
}


def puzzle1():
    lines = open("day24.txt").read().split('\n')
    flips = collections.defaultdict(int)
    for line in lines:
        dirs = re.findall('e|se|sw|w|nw|ne', line)
        x, y = 0, 0
        for d in dirs:
            char = grid[d]
            x += char[0]
            y += char[1]
        flips[(x, y)] += 1
    return sum(1 for k, v in flips.items() if v % 2 == 1)


def step(flips):
    neighbours = collections.defaultdict(int)
    for k, v in flips.items():
        if v % 2 == 0:
            continue
        for adj in grid.values():
            pt = (k[0] + adj[0], k[1] + adj[1])
            neighbours[pt] += 1

    newflips = {}
    for k, v in flips.items():
        if v % 2 == 1:
            if neighbours.get(k, 0) not in (1, 2):
                # flip to white
                pass
            else:
                newflips[k] = 1
    for k, v in neighbours.items():
        if v == 2 and flips.get(k, 0) % 2 == 0:
            newflips[k] = 1
    return newflips


def puzzle2():
    lines = open("day24.txt").read().split('\n')
    flips = collections.defaultdict(int)
    for line in lines:
        dirs = re.findall('e|se|sw|w|nw|ne', line)
        x, y = 0, 0
        for d in dirs:
            char = grid[d]
            x += char[0]
            y += char[1]
        flips[(x, y)] += 1
    for i in range(100):
        flips = step(flips)
    return sum(1 for k, v in flips.items() if v % 2 == 1)


if __name__ == '__main__':
    start_puzzle1 = int(round(time.time() * 1000))
    res_puzzle1 = puzzle1()
    end_puzzle1 = int(round(time.time() * 1000))
    print("Puzzle 1: " + str(res_puzzle1) + ". Took: " + str((end_puzzle1 - start_puzzle1)))
    start_puzzle2 = int(round(time.time() * 1000))
    res_puzzle2 = puzzle2()
    end_puzzle2 = int(round(time.time() * 1000))
    print("Puzzle 2: " + str(res_puzzle2) + ". Took: " + str((end_puzzle2 - start_puzzle2)))
