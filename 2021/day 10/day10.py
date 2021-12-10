import time
from collections import deque

close = {")", "]", "}", ">"}
pairs = {")": "(", "]": "[", "}": "{", ">": "<"}
points1 = {")": 3, "]": 57, "}": 1197, ">": 25137}


def puzzle1():
    res = 0
    for line in open('day10.txt').read().split("\n"):
        stack = deque()
        for i in line:
            if i not in close:
                stack.append(i)
            else:
                last = stack.pop()
                if last != pairs[i]:
                    res += points1[i]
    return res


points2 = {"(": 1, "[": 2, "{": 3, "<": 4}


def puzzle2():
    res = []
    for line in open('day10.txt').read().split("\n"):
        stack = deque()
        corrupted = False
        for i in line:
            if i not in close:
                stack.append(i)
            else:
                last = stack.pop()
                if last != pairs[i]:
                    corrupted = True
                    break
        if not corrupted:
            score = 0
            while len(stack) > 0:
                score *= 5
                score += points2[stack.pop()]
            res.append(score)
    res.sort()
    return res[int(len(res)/2)]


if __name__ == '__main__':
    start_puzzle1 = int(round(time.time() * 1000))
    res_puzzle1 = puzzle1()
    end_puzzle1 = int(round(time.time() * 1000))
    print("Puzzle 1: " + str(res_puzzle1) + ". Took: " + str((end_puzzle1 - start_puzzle1)))
    start_puzzle2 = int(round(time.time() * 1000))
    res_puzzle2 = puzzle2()
    end_puzzle2 = int(round(time.time() * 1000))
    print("Puzzle 2: " + str(res_puzzle2) + ". Took: " + str((end_puzzle2 - start_puzzle2)))
