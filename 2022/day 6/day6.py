import time


def puzzle1():
    package_length = 4
    data = open('day6.txt').read().split("\n\n")[0]
    for i in range(package_length, len(data)):
        if len({data[j] for j in range(i - package_length + 1, i + 1)}) == package_length:
            return i + 1


def puzzle2():
    package_length = 14
    data = open('day6.txt').read().split("\n\n")[0]
    for i in range(package_length, len(data)):
        if len({data[j] for j in range(i - package_length + 1, i + 1)}) == package_length:
            return i + 1


if __name__ == '__main__':
    start_puzzle1 = int(round(time.time() * 1000))
    res_puzzle1 = puzzle1()
    end_puzzle1 = int(round(time.time() * 1000))
    print("Puzzle 1: " + str(res_puzzle1) + ". Took: " + str((end_puzzle1 - start_puzzle1)))
    start_puzzle2 = int(round(time.time() * 1000))
    res_puzzle2 = puzzle2()
    end_puzzle2 = int(round(time.time() * 1000))
    print("Puzzle 2: " + str(res_puzzle2) + ". Took: " + str((end_puzzle2 - start_puzzle2)))
