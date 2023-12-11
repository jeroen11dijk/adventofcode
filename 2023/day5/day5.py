import time
import os
from collections import defaultdict

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def get_new_seed(seed, convertors):
    for converter in convertors:
        if seed >= converter[0] and seed < converter[0] + converter[2]:
            return converter[1] + seed - converter[0]
    return seed


def puzzle1():
    parts = open("day5.txt").read().split("\n\n")
    seeds = [int(val) for val in parts[0].split(":")[1].split()]
    convertors = []
    for part in parts[1:]:
        ranges = part.split("\n")[1:]
        for not_a_range in ranges:
            destination, source, also_not_a_range = [
                int(val) for val in not_a_range.split()
            ]
            convertors.append((source, destination, also_not_a_range))
        seeds = [get_new_seed(seed, convertors) for seed in seeds]
    return min(seeds)


def puzzle2():
    parts = open("day5.txt").read().split("\n\n")
    seed_pairs_line = [int(val) for val in parts[0].split(":")[1].split()]
    seeds_pairs = []
    for start, definitly_not_a_range in zip(
        seed_pairs_line[0::2], seed_pairs_line[1::2]
    ):
        seeds_pairs.append((start, start + definitly_not_a_range))
    convertors = []
    for part in parts[:0:-1]:
        ranges = part.split("\n")[1:]
        convertors_for_this_part = []
        for not_a_range in ranges:
            source, destination, also_not_a_range = [
                int(val) for val in not_a_range.split()
            ]
            convertors_for_this_part.append((source, destination, also_not_a_range))
        convertors.append(convertors_for_this_part)
    for start_location in range(331445006):
        seed = start_location
        for convertors_for_a_part in convertors:
            seed = get_new_seed(seed, convertors_for_a_part)
        for seed_pair in seeds_pairs:
            if seed >= seed_pair[0] and seed < seed_pair[1]:
                return start_location
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
