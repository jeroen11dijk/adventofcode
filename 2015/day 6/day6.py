import time
from collections import defaultdict


def puzzle1():
    res = set()
    for line in open('day6.txt').read().splitlines():
        if line.split()[0] == "toggle":
            topleft = [int(x) for x in line.split()[1].split(",")]
            bottomright = [int(x) for x in line.split()[3].split(",")]
        else:
            topleft = [int(x) for x in line.split()[2].split(",")]
            bottomright = [int(x) for x in line.split()[4].split(",")]
        for x in range(topleft[0], bottomright[0] + 1):
            for y in range(topleft[1], bottomright[1] + 1):
                if line.split()[0] == "toggle":
                    if (x, y) in res:
                        res.remove((x, y))
                    else:
                        res.add((x, y))
                if line.split()[1] == "off":
                    if (x, y) in res:
                        res.remove((x, y))
                if line.split()[1] == "on":
                    res.add((x, y))
    return len(res)


def puzzle2():
    res = defaultdict(int)
    for line in open('day6.txt').read().splitlines():
        if line.split()[0] == "toggle":
            topleft = [int(x) for x in line.split()[1].split(",")]
            bottomright = [int(x) for x in line.split()[3].split(",")]
        else:
            topleft = [int(x) for x in line.split()[2].split(",")]
            bottomright = [int(x) for x in line.split()[4].split(",")]
        for x in range(topleft[0], bottomright[0] + 1):
            for y in range(topleft[1], bottomright[1] + 1):
                if line.split()[0] == "toggle":
                    res[(x, y)] += 2
                if line.split()[1] == "off":
                    res[(x, y)] -= 1
                    res[(x, y)] = max(res[(x, y)], 0)
                if line.split()[1] == "on":
                    res[(x, y)] += 1
    return sum(res.values())


if __name__ == '__main__':
    start_puzzle1 = int(round(time.time() * 1000))
    # res_puzzle1 = puzzle1()
    end_puzzle1 = int(round(time.time() * 1000))
    # print("Puzzle 1: " + str(res_puzzle1) + ". Took: " + str((end_puzzle1 - start_puzzle1)))
    start_puzzle2 = int(round(time.time() * 1000))
    res_puzzle2 = puzzle2()
    end_puzzle2 = int(round(time.time() * 1000))
    print("Puzzle 2: " + str(res_puzzle2) + ". Took: " + str((end_puzzle2 - start_puzzle2)))
