import time


def convertToNumber(string, upper):
    res = 0
    for i, char in enumerate(reversed(string[0:7])):
        if char == upper:
            res += 2 ** i
    return res


def puzzle1():
    res = 0
    for line in open('day5.txt'):
        seatId = convertToNumber(line[0:7], 'B') * 8 + convertToNumber(line[7:10], 'R')
        res = max(res, seatId)
    return res


def puzzle2():
    seatIds = set()
    for line in open('day5.txt'):
        seatId = convertToNumber(line[0:7], 'B') * 8 + convertToNumber(line[7:10], 'R')
        seatIds.add(seatId)
    for i in range(min(seatIds), max(seatIds)):
        if i not in seatIds:
            return i


if __name__ == '__main__':
    start_puzzle1 = int(round(time.time() * 1000))
    res_puzzle1 = puzzle1()
    end_puzzle1 = int(round(time.time() * 1000))
    print("Puzzle 1: " + str(res_puzzle1) + ". Took: " + str((end_puzzle1 - start_puzzle1)))
    start_puzzle2 = int(round(time.time() * 1000))
    res_puzzle2 = puzzle2()
    end_puzzle2 = int(round(time.time() * 1000))
    print("Puzzle 2: " + str(res_puzzle2) + ". Took: " + str((end_puzzle2 - start_puzzle2)))
