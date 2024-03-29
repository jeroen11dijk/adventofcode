import time
from collections import defaultdict


def get_calories():
    res, person = defaultdict(int), 0
    values = [None if i == '' else int(i) for i in open('day1.txt').read().split("\n")]
    for i in values:
        if i is not None:
            res[person] += i
        else:
            person += 1
    return res


def puzzle1():
    return max(get_calories().values())


def puzzle2():
    return sum(sorted(list(get_calories().values()))[-3:])


if __name__ == '__main__':
    start_puzzle1 = int(round(time.time() * 1000))
    res_puzzle1 = puzzle1()
    end_puzzle1 = int(round(time.time() * 1000))
    print("Puzzle 1: " + str(res_puzzle1) + ". Took: " + str((end_puzzle1 - start_puzzle1)))
    start_puzzle2 = int(round(time.time() * 1000))
    res_puzzle2 = puzzle2()
    end_puzzle2 = int(round(time.time() * 1000))
    print("Puzzle 2: " + str(res_puzzle2) + ". Took: " + str((end_puzzle2 - start_puzzle2)))
