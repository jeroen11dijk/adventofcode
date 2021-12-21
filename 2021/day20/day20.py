import time
from functools import lru_cache

lookup_lines, grid_lines = open("day20.txt").read().split('\n\n')
lookup = ""
for i in lookup_lines.split('\n'):
    for b in i:
        lookup += str(int(b == "#"))
grid = [[0] * (len(grid_lines.split('\n')[0])) for _ in range(len(grid_lines.split('\n')))]
for i, row in enumerate(grid_lines.split('\n')):
    row = row.strip()
    for j, value in enumerate(row):
        grid[i][j] = int(value == "#")


@lru_cache(maxsize=None)
def recursive(x, y, time):
    if time == 0:
        if 0 <= x < len(grid) and 0 <= y < len(grid):
            return int(grid[x][y])
        else:
            return 0
    return int(lookup[recursive(x + 1, y + 1, time - 1) + 2 * recursive(x + 1, y, time - 1, ) +
                      4 * recursive(x + 1, y - 1, time - 1,) + 8 * recursive(x, y + 1, time - 1, ) +
                      16 * recursive(x, y, time - 1, ) + 32 * recursive(x, y - 1, time - 1) +
                      64 * recursive(x - 1, y + 1, time - 1, ) + 128 * recursive(x - 1, y, time - 1) +
                      256 * recursive(x - 1, y - 1,time - 1, )])


def puzzle1():
    res = 0
    steps = 2
    for x in range(-steps, len(grid) + steps):
        for y in range(-steps, len(grid) + steps):
            res += recursive(x, y, steps)
    return res


def puzzle2():
    res = 0
    steps = 50
    for x in range(-steps, len(grid) + steps):
        for y in range(-steps, len(grid) + steps):
            print(x, y)
            res += recursive(x, y, steps)
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
