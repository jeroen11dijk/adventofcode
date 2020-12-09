import time


def valid(preamble, number):
    for first in preamble:
        for second in preamble:
            if first + second == number:
                return True
    return False


def puzzle1():
    allNumbers = [int(number) for number in open('day9.txt').read().split("\n")]
    preamble = allNumbers[0:25]
    for i in range(25, len(allNumbers)):
        number = allNumbers[i]
        if valid(preamble, number):
            preamble[i % 25] = number
        else:
            return number


def puzzle2():
    allNumbers = [int(number) for number in open('day9.txt').read().split("\n")]
    number = puzzle1()
    for startIndex in range(len(allNumbers)):
        res = allNumbers[startIndex]
        values = [allNumbers[startIndex]]
        for index in range(startIndex + 1, len(allNumbers)):
            res += allNumbers[index]
            values.append(allNumbers[index])
            if res == number:
                return min(values) + max(values)
            if res > number:
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
