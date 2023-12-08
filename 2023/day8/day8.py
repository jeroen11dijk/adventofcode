import time
import os
from math import gcd


os.chdir(os.path.dirname(os.path.abspath(__file__)))


def puzzle1():
    instructions, map_lines = open("day8.txt").read().split("\n\n")
    map = {}
    for line in map_lines.splitlines():
        start, targets = line.split(" = ")
        left, right = targets[1:-1].split(", ")
        map[start] = (left, right)
    curr = "AAA"
    steps = 0
    while True:
        for instruction in instructions:
            steps += 1
            if instruction == "L":
                curr = map[curr][0]
            else:
                curr = map[curr][1]
            if curr == "ZZZ":
                return steps


def puzzle2():
    instructions, map_lines = open("day8.txt").read().split("\n\n")
    map = {}
    curr_locations = []
    for line in map_lines.splitlines():
        start, targets = line.split(" = ")
        left, right = targets[1:-1].split(", ")
        map[start] = (left, right)
        if start[-1] == "A":
            curr_locations.append(start)
    cycles = [0] * len(curr_locations)
    steps = 0
    while True:
        for instruction in instructions:
            steps += 1
            for i, curr in enumerate(curr_locations):
                if instruction == "L":
                    curr_locations[i] = map[curr][0]
                else:
                    curr_locations[i] = map[curr][1]
                if curr[-1] == "Z" and cycles[i] == 0:
                    cycles[i] = steps - 1
            if all(val != 0 for val in cycles):
                lcm = 1
                for i in cycles:
                    lcm = lcm*i//gcd(lcm, i)
                return lcm


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
