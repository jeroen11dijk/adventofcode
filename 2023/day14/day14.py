import time
import os
import numpy as np

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def roll_stones(lines, left_to_right):
    if not left_to_right:
        for line in lines:
            line.reverse()
    for line in lines:
        made_change = True
        while made_change:
            made_change = False
            for i in range(1, len(line)):
                if line[i] == "O" and line[i - 1] == ".":
                    made_change = True
                    line[i - 1] = "O"
                    line[i] = "."
    if not left_to_right:
        for line in lines:
            line.reverse()
    return lines


def puzzle1():
    res = 0
    lines = [[] for _ in range(len(open("day14.txt").read().splitlines()[0]))]
    for line in open("day14.txt").read().splitlines():
        for i, val in enumerate(line):
            lines[i].append(val)
    lines = roll_stones(lines, True)
    for line in lines:
        line.reverse()
        res += sum([i + 1 if line[i] == "O" else 0 for i in range(len(line))])
    return res


def puzzle2():
    res = 0
    lines = [[] for _ in range(len(open("day14.txt").read().splitlines()[0]))]
    for line in open("day14.txt").read().splitlines():
        for i, val in enumerate(line):
            lines[i].append(val)
    dharok_axe = {}
    for i in range(1, 1000000000):
        lines = roll_stones(lines, True)
        lines = np.array(lines).T.tolist()
        lines = roll_stones(lines, True)
        lines = np.array(lines).T.tolist()
        lines = roll_stones(lines, False)
        lines = np.array(lines).T.tolist()
        lines = roll_stones(lines, False)
        lines = np.array(lines).T.tolist()
        hashable_lines = tuple(tuple(line) for line in lines)
        if hashable_lines in dharok_axe:
            original = dharok_axe[hashable_lines]
            loop = i - original
            to_go = 1000000000 - original
            skip_loops = int(to_go / loop)
            new_i = original + skip_loops * loop
            break
        dharok_axe[hashable_lines] = i
    for i in range(new_i + 1, 1000000001):
        lines = roll_stones(lines, True)
        lines = np.array(lines).T.tolist()
        lines = roll_stones(lines, True)
        lines = np.array(lines).T.tolist()
        lines = roll_stones(lines, False)
        lines = np.array(lines).T.tolist()
        lines = roll_stones(lines, False)
        lines = np.array(lines).T.tolist()
    for line in lines:
        line.reverse()
        res += sum([i + 1 if line[i] == "O" else 0 for i in range(len(line))])
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
