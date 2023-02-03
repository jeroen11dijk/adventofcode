import time


def puzzle1():
    x, y = 0, 0
    for line in open('day2.txt').readlines():
        command, value = line.split()
        if command == "forward":
            x += int(value)
        if command == "down":
            y += int(value)
        if command == "up":
            y -= int(value)
    return x * y


def puzzle2():
    x, y, aim = 0, 0, 0
    for line in open('day2.txt').readlines():
        command, value = line.split()
        if command == "forward":
            x += int(value)
            y += int(value)*aim
        if command == "down":
            aim += int(value)
        if command == "up":
            aim -= int(value)
    return x * y


if __name__ == '__main__':
    start_puzzle1 = int(round(time.time() * 1000))
    res_puzzle1 = puzzle1()
    end_puzzle1 = int(round(time.time() * 1000))
    print("Puzzle 1: " + str(res_puzzle1) + ". Took: " + str((end_puzzle1 - start_puzzle1)))
    start_puzzle2 = int(round(time.time() * 1000))
    res_puzzle2 = puzzle2()
    end_puzzle2 = int(round(time.time() * 1000))
    print("Puzzle 2: " + str(res_puzzle2) + ". Took: " + str((end_puzzle2 - start_puzzle2)))
