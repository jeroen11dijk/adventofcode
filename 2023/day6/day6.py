import time
import os
from collections import defaultdict

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def puzzle1():
    res = 1
    times, distances = open("day6.txt").read().split("\n")
    times = [int(val) for val in times.split()[1:]]
    distances = [int(val) for val in distances.split()[1:]]
    for time, distance in zip(times, distances):
        n_ways_to_win = 0
        for i in range(time):
            if i*(time-i) > distance:
                n_ways_to_win += 1
        res *= n_ways_to_win
    return res


def puzzle2():
    time = 47986698
    distance = 400121310111540
    res = 0
    for i in range(time):
        if i*(time-i) > distance:
            res += 1
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
