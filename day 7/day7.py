import time
from collections import deque


def create_dictionary():
    dictionary = {}
    for line in open('day7.txt'):
        key = line.split(' ')[0] + " " + line.split(' ')[1]
        value = {}
        if line.split(' ')[4] == "no":
            dictionary[key] = {}
        else:
            for i in range(4, len(line.split(' ')), 4):
                value[line.split(' ')[i + 1] + " " + line.split(' ')[i + 2]] = line.split(' ')[i]
            dictionary[key] = value
    return dictionary


def tree_search(dictionary, key):
    if "shiny gold" in dictionary[key]:
        return 1
    else:
        for child in dictionary[key].keys():
            if tree_search(dictionary, child):
                return 1
    return 0


def shiny_bag_search(dictionary, key):
    if not dictionary[key]:
        return 1
    return sum([int(v)*shiny_bag_search(dictionary, k) for k, v in dictionary[key].items()]) + 1


def puzzle1():
    res = 0
    for key in create_dictionary().keys():
        res += tree_search(create_dictionary(), key)


def puzzle2():
    res = 0
    for key in create_dictionary()["shiny gold"]:
        res += int(create_dictionary()["shiny gold"][key]) * shiny_bag_search(create_dictionary(), key)
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
