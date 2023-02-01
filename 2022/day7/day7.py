import time
from collections import defaultdict


def generate_tree():
    path = []
    data = defaultdict(int)
    for line in open('day7.txt').read().splitlines():
        command = line.split()
        if command[1] == "cd":
            if command[2] == "..":
                path.pop(-1)
            else:
                path.append(command[2])
        if command[0].isdigit():
            for i in range(1, len(path) + 1):
                data[tuple(path[:i])] += int(command[0])
    return data


def puzzle1():
    data = generate_tree()
    return sum([i for i in data.values() if i < 100000])


def puzzle2():
    data = generate_tree()
    memory_needed = 30000000 - (70000000 - data[("/",)])
    return min([i for i in data.values() if i > memory_needed])

if __name__ == '__main__':
    start_puzzle1 = int(round(time.time() * 1000))
    res_puzzle1 = puzzle1()
    end_puzzle1 = int(round(time.time() * 1000))
    print("Puzzle 1: " + str(res_puzzle1) + ". Took: " + str((end_puzzle1 - start_puzzle1)))
    start_puzzle2 = int(round(time.time() * 1000))
    res_puzzle2 = puzzle2()
    end_puzzle2 = int(round(time.time() * 1000))
    print("Puzzle 2: " + str(res_puzzle2) + ". Took: " + str((end_puzzle2 - start_puzzle2)))
