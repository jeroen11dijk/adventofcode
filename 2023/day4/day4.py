import time
import os
from collections import defaultdict

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def puzzle1():
    res = 0
    for line in open("day4.txt").readlines():
        winning, got = line.strip().split("|")
        winning_numbers = {int(number) for number in winning.split(":")[1].split()}
        my_numbers = {int(number) for number in got.split()}
        n_winning_numbers = len(winning_numbers.intersection(my_numbers)) - 1
        if n_winning_numbers > -1:
            res += 2 ** max((len(winning_numbers.intersection(my_numbers)) - 1), 0)
    return res


def puzzle2():
    res = 0
    scratchards = defaultdict(lambda: 1)
    for i, line in enumerate(open("day4.txt").readlines()):
        index = i + 1
        winning, got = line.strip().split("|")
        winning_numbers = {int(number) for number in winning.split(":")[1].split()}
        my_numbers = {int(number) for number in got.split()}
        matching_numbers = len(winning_numbers.intersection(my_numbers))
        for j in range(index + 1, index+1 + matching_numbers):
            scratchards[j] += scratchards[index]
    for i in range(len(open("day4.txt").readlines())):
        res += scratchards[i+1]    
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
