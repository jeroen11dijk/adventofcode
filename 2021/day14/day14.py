import re
import time
from collections import defaultdict


def code(timesteps):
    rules = {}
    pairs = defaultdict(int)
    counts = defaultdict(int)
    for i, line in enumerate(open('day14.txt').read().splitlines()):
        if i == 0:
            start = re.match(r'[A-Z]+', line).group(0)
        elif i > 1:
            rules[re.findall(r'[A-Z]+', line)[0]] = re.findall(r'[A-Z]+', line)[1]
    for i, char in enumerate(start):
        counts[char] += 1
        if i < len(start) - 1:
            pairs[str(char + start[i + 1])] += 1
    for _ in range(timesteps):
        new_pairs = defaultdict(int)
        for pair in pairs:
            new_pairs[str(pair[0] + rules[pair])] += pairs[pair]
            new_pairs[str(rules[pair] + pair[1])] += pairs[pair]
            counts[rules[pair]] += pairs[pair]
        pairs = new_pairs
    return max(counts.values()) - min(counts.values())


def puzzle1():
    return code(10)


def puzzle2():
    return code(40)


if __name__ == '__main__':
    start_puzzle1 = int(round(time.time() * 1000))
    res_puzzle1 = puzzle1()
    end_puzzle1 = int(round(time.time() * 1000))
    print("Puzzle 1: " + str(res_puzzle1) + ". Took: " + str((end_puzzle1 - start_puzzle1)))
    start_puzzle2 = int(round(time.time() * 1000))
    res_puzzle2 = puzzle2()
    end_puzzle2 = int(round(time.time() * 1000))
    print("Puzzle 2: " + str(res_puzzle2) + ". Took: " + str((end_puzzle2 - start_puzzle2)))
