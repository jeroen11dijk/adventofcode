import time
import os
from math import gcd
from itertools import combinations

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def puzzle1():
    res = 0
    grid = []
    double_x = []
    for i, line in enumerate(open("day11.txt").readlines()):
        grid.append([])
        for val in line.strip():
            grid[i].append(val)
        if all(val == "." for val in grid[i]):
            double_x.append(i)
    double_y = []
    for j in range(len(grid[0])):
        if all(line[j] == "." for line in grid):
            double_y.append(j)

    galaxies = []
    x = 0
    y = 0
    print(double_x, double_y)
    for i, row in enumerate(grid):
        if i in double_x:
            x += 2
        else:
            x += 1
        for j, val in enumerate(row):
            if j in double_y:
                y += 2
            else:
                y += 1
            if val == "#":
                galaxies.append((x, y))
    print(galaxies)
    for pair in list(combinations(galaxies, 2)):
        res += abs(pair[0][0] - pair[1][0]) + abs(pair[0][1] - pair[1][1])
    return res


def puzzle2():
    return 0


if __name__ == "__main__":
    start_puzzle1 = int(round(time.time() * 1000))
    res_puzzle1 = puzzle1()
    end_puzzle1 = int(round(time.time() * 1000))
    print(
        "Puzzle 1: "
        + str(res_puzzle1)
        + ". Took: "
        + str((end_puzzle1 - start_puzzle1))
    )
    start_puzzle2 = int(round(time.time() * 1000))
    res_puzzle2 = puzzle2()
    end_puzzle2 = int(round(time.time() * 1000))
    print(
        "Puzzle 2: "
        + str(res_puzzle2)
        + ". Took: "
        + str((end_puzzle2 - start_puzzle2))
    )
