import time
import operator


def move(head, tail):
    if max(abs(head[0] - tail[0]), abs(head[1] - tail[1])) > 1:
        if head[0] > tail[0]:
            tail[0] += 1
        elif head[0] < tail[0]:
            tail[0] -= 1
        if head[1] > tail[1]:
            tail[1] += 1
        elif head[1] < tail[1]:
            tail[1] -= 1
    return tail


directions = {"U": (0, 1), "D": (0, -1), "R": (1, 0), "L": (-1, 0)}


def puzzle1():
    head, tail = [0, 0], [0, 0]
    visited = {(0, 0)}
    for line in open('day9.txt').read().splitlines():
        direction, amount = line.split()
        for i in range(int(amount)):
            head = list(map(operator.add, head, directions[direction]))
            tail = move(head, tail)
            visited.add(tuple(tail))
    return len(visited)


def puzzle2():
    rope = [[0, 0] for _ in range(10)]
    visited = {(0, 0)}
    for line in open('day9.txt').read().splitlines():
        direction, amount = line.split()
        for i in range(int(amount)):
            rope[0] = list(map(operator.add, rope[0], directions[direction]))
            for j in range(1, len(rope)):
                rope[j] = move(rope[j - 1], rope[j])
            visited.add(tuple(rope[-1]))
    return len(visited)


if __name__ == '__main__':
    start_puzzle1 = int(round(time.time() * 1000))
    res_puzzle1 = puzzle1()
    end_puzzle1 = int(round(time.time() * 1000))
    print("Puzzle 1: " + str(res_puzzle1) + ". Took: " + str((end_puzzle1 - start_puzzle1)))
    start_puzzle2 = int(round(time.time() * 1000))
    res_puzzle2 = puzzle2()
    end_puzzle2 = int(round(time.time() * 1000))
    print("Puzzle 2: " + str(res_puzzle2) + ". Took: " + str((end_puzzle2 - start_puzzle2)))
