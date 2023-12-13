import time
import os
from math import gcd
from itertools import combinations

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def differences(one, two):
    return sum(1 for x, y in zip(one, two) if x != y)


def find_mirrors(input, must_clean):
    for i in range(len(input) - 1):
        left = i
        right = i + 1
        total_differences = 0
        while left >= 0 and right < len(input):
            total_differences += differences(input[left], input[right])
            left -= 1
            right += 1
        if must_clean and total_differences == 1:
            return i + 1
        if not must_clean and total_differences == 0:
            return i + 1
    return 0


def puzzle1():
    res = 0
    for line in open("day13.txt").read().split("\n\n"):
        rows = []
        columns = [[] for _ in range(len(line.split("\n")[0]))]
        for row in line.split("\n"):
            rows.append(row)
            for j, val in enumerate(row):
                columns[j].append(val)
        res += 100 * find_mirrors(rows, False) + find_mirrors(columns, False)
    return res


def puzzle2():
    res = 0
    for line in open("day13.txt").read().split("\n\n"):
        rows = []
        columns = [[] for _ in range(len(line.split("\n")[0]))]
        for row in line.split("\n"):
            rows.append(row)
            for j, val in enumerate(row):
                columns[j].append(val)
        res += 100 * find_mirrors(rows, True) + find_mirrors(columns, True)
    return res


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
