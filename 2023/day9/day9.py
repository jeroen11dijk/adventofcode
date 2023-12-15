import time
import os
from math import gcd


os.chdir(os.path.dirname(os.path.abspath(__file__)))


def puzzle1():
    res = 0
    for line in open("day9.txt").read().splitlines():
        curr = [int(val) for val in line.split()]
        pyramid = [curr]
        while not all(val == 0 for val in curr):
            next_line = []
            for i in range(len(curr)-1):
                next_line.append(curr[i+1]-curr[i])
            curr = next_line
            pyramid.append(curr)
        last_value_added = 0
        for i in range(len(pyramid)):
            if i == 0:
                pyramid[-1].append(0)
                continue
            else:
                last_value_added = last_value_added + pyramid[-i-1][-1]
                pyramid[-i-1].append(last_value_added)                
        res += last_value_added
    return res

def puzzle2():
    res = 0
    for line in open("day9.txt").read().splitlines():
        curr = [int(val) for val in line.split()]
        pyramid = [curr]
        while not all(val == 0 for val in curr):
            next_line = []
            for i in range(len(curr)-1):
                next_line.append(curr[i+1]-curr[i])
            curr = next_line
            pyramid.append(curr)
        last_value_added = 0
        for i in range(len(pyramid)):
            if i == 0:
                pyramid.insert(0,0)
                continue
            else:
                last_value_added = pyramid[-i-1][0] - last_value_added
                pyramid[-i-1].insert(0, last_value_added)                
        res += last_value_added
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
