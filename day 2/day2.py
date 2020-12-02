import time


def puzzle1():
    res = 0
    with open('day2.txt') as f:
        for line in f:
            minmax, char, password = line.replace(':', ' ').split()
            min, max = map(int, minmax.split("-"))
            res += min <= password.count(char) <= max
    return res


def puzzle2():
    res = 0
    with open('day2.txt') as f:
        for line in f:
            minmax, char, password = line.replace(':', ' ').split()
            first, second = map(int, minmax.split("-"))
            res += (password[first - 1] == char) ^ (password[second - 1] == char)
    return res


if __name__ == '__main__':
    start_puzzle1 = int(round(time.time() * 1000))
    res_puzzle1 = puzzle1()
    end_puzzle1 = int(round(time.time() * 1000))
    print("Puzzle 1 : " + str(res_puzzle1) + ". Took: " + str((end_puzzle1 - start_puzzle1)))
    start_puzzle2 = int(round(time.time() * 1000))
    res_puzzle2 = puzzle2()
    end_puzzle2 = int(round(time.time() * 1000))
    print("Puzzle 1 : " + str(res_puzzle2) + ". Took: " + str((end_puzzle2 - start_puzzle2)))
