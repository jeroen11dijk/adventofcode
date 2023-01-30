import re
import time


def puzzle1():
    yline = set()
    beacons = set()
    for line in open('day15.txt').read().splitlines():
        x1, y1, x2, y2 = [int(x) for x in re.findall(r'-?\d+', line)]
        dist = abs(x1 - x2) + abs(y1 - y2)
        xrange = dist - abs(2000000 - y1)
        if xrange > 0:
            for x in range(x1 - xrange, x1 + xrange + 1):
                yline.add((x, 2000000))
        beacons.add((x2, y2))
    return len(yline - beacons)


def puzzle2():
    distances = {}
    for line in open('day15.txt').read().splitlines():
        x1, y1, x2, y2 = [int(x) for x in re.findall(r'-?\d+', line)]
        distances[(x1, y1)] = abs(x1 - x2) + abs(y1 - y2)
    for y in range(1, 4000000):
        x = 1
        while x <= 4000000:
            for i, node in enumerate(distances):
                if abs(node[0] - x) + abs(node[1] - y) <= distances[node]:
                    xrange = distances[node] - abs(y - node[1])
                    x = node[0] + xrange + 1
                    break
                if i == len(distances) - 1:
                    return x * 4000000 + y


if __name__ == '__main__':
    start_puzzle1 = int(round(time.time() * 1000))
    res_puzzle1 = puzzle1()
    end_puzzle1 = int(round(time.time() * 1000))
    print("Puzzle 1: " + str(res_puzzle1) + ". Took: " + str((end_puzzle1 - start_puzzle1)))
    start_puzzle2 = int(round(time.time() * 1000))
    res_puzzle2 = puzzle2()
    end_puzzle2 = int(round(time.time() * 1000))
    print("Puzzle 2: " + str(res_puzzle2) + ". Took: " + str((end_puzzle2 - start_puzzle2)))
