import time
from collections import defaultdict


def puzzle(target):
    starting_numbers = list(map(int, open('day15.txt').read().split(",")))
    occurences = defaultdict(list, {value: [i + 1] for i, value in enumerate(starting_numbers)})
    last_number = starting_numbers[-1]
    len_starting_numbers = len(starting_numbers)
    for i in range(len_starting_numbers + 1, target + 1):
        if len(occurences[last_number]) > 1:
            last_number = occurences[last_number][-1] - occurences[last_number][-2]
        else:
            last_number = 0
        occurences[last_number].append(i)
    return last_number


if __name__ == '__main__':
    start_puzzle1 = int(round(time.time() * 1000))
    res_puzzle1 = puzzle(2020)
    end_puzzle1 = int(round(time.time() * 1000))
    print("Puzzle 1: " + str(res_puzzle1) + ". Took: " + str((end_puzzle1 - start_puzzle1)))
    start_puzzle2 = int(round(time.time() * 1000))
    res_puzzle2 = puzzle(30000000)
    end_puzzle2 = int(round(time.time() * 1000))
    print("Puzzle 2: " + str(res_puzzle2) + ". Took: " + str((end_puzzle2 - start_puzzle2)))
