import re
import time


def get_rocks():
    rocks = set()
    floor = 0
    for line in open('day14.txt').read().splitlines():
        lines = re.findall(r'\d+,\d+', line)
        for i in range(1, len(lines)):
            x1, y1 = [int(x) for x in lines[i - 1].split(",")]
            x2, y2 = [int(x) for x in lines[i].split(",")]
            floor = max(y1, y2, floor)
            if x1 == x2:
                for y in range(min(y1, y2), max(y1, y2) + 1):
                    rocks.add((x1, y))
            else:
                for x in range(min(x1, x2), max(x1, x2) + 1):
                    rocks.add((x, y1))
    return rocks, floor


def puzzle1():
    rocks, floor = get_rocks()
    sands = 0
    sand = [500, 0]
    while True:
        if sand[1] > floor:
            return sands
        if not (sand[0], sand[1] + 1) in rocks:
            sand = [sand[0], sand[1] + 1]
        else:
            if not (sand[0] - 1, sand[1] + 1) in rocks:
                sand = [sand[0] - 1, sand[1] + 1]
            elif not (sand[0] + 1, sand[1] + 1) in rocks:
                sand = [sand[0] + 1, sand[1] + 1]
            else:
                rocks.add(tuple(sand))
                sand = [500, 0]
                sands += 1


def puzzle2():
    rocks, floor = get_rocks()
    floor += 2
    sands = 1
    sand = [500, 0]
    while True:
        if sand[1] + 1 == floor:
            rocks.add(tuple(sand))
            sand = [500, 0]
            sands += 1
        if not (sand[0], sand[1] + 1) in rocks:
            sand = [sand[0], sand[1] + 1]
        else:
            if not (sand[0] - 1, sand[1] + 1) in rocks:
                sand = [sand[0] - 1, sand[1] + 1]
            elif not (sand[0] + 1, sand[1] + 1) in rocks:
                sand = [sand[0] + 1, sand[1] + 1]
            else:
                if sand == [500, 0]:
                    return sands
                rocks.add(tuple(sand))
                sand = [500, 0]
                sands += 1


if __name__ == '__main__':
    start_puzzle1 = int(round(time.time() * 1000))
    res_puzzle1 = puzzle1()
    end_puzzle1 = int(round(time.time() * 1000))
    print("Puzzle 1: " + str(res_puzzle1) + ". Took: " + str((end_puzzle1 - start_puzzle1)))
    start_puzzle2 = int(round(time.time() * 1000))
    res_puzzle2 = puzzle2()
    end_puzzle2 = int(round(time.time() * 1000))
    print("Puzzle 2: " + str(res_puzzle2) + ". Took: " + str((end_puzzle2 - start_puzzle2)))
