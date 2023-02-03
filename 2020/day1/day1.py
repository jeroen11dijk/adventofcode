import time


def puzzle1():
    with open('day1.txt') as f:
        numbers = [int(x) for x in f.read().splitlines()]
        numbers.sort()

    for first in numbers:
        for second in reversed(numbers):
            if first + second == 2020:
                return first * second
            if first + second < 2020:
                break


def puzzle2():
    with open('day1.txt') as f:
        numbers = [int(x) for x in f.read().splitlines()]
        numbers.sort()

    for first in numbers:
        for second in reversed(numbers):
            if first + second < 2020:
                for third in numbers:
                    if first + second + third == 2020:
                        return first * second * third
                    if first + second + third > 2020:
                        break


if __name__ == '__main__':
    start_puzzle1 = int(round(time.time() * 1000))
    res_puzzle1 = puzzle1()
    end_puzzle1 = int(round(time.time() * 1000))
    print("Puzzle 1: " + str(res_puzzle1) + ". Took: " + str((end_puzzle1 - start_puzzle1)))
    start_puzzle2 = int(round(time.time() * 1000))
    res_puzzle2 = puzzle2()
    end_puzzle2 = int(round(time.time() * 1000))
    print("Puzzle 2: " + str(res_puzzle2) + ". Took: " + str((end_puzzle2 - start_puzzle2)))
