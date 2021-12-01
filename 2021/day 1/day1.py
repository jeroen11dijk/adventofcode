import time


def puzzle1():
    res = 0
    values = [int(i) for i in open('day1.txt').read().split("\n")]
    for i in range(len(values)):
        if i != 0 and values[i] > values[i-1]:
            res += 1
    return res



def puzzle2():
    res = 0
    values = [int(i) for i in open('day1.txt').read().split("\n")]
    for i in range(2, len(values) - 1):
        print(sum([values[i], values[i+1], values[i-1]]))
        print(sum([values[i], values[i-1], values[i-2]]))
        if sum([values[i], values[i+1], values[i-1]]) > sum([values[i], values[i-1], values[i-2]]):
            res += 1
    return res


if __name__ == '__main__':
    start_puzzle1 = int(round(time.time() * 1000))
    res_puzzle1 = puzzle1()
    end_puzzle1 = int(round(time.time() * 1000))
    print("Puzzle 1: " + str(res_puzzle1) + ". Took: " + str((end_puzzle1 - start_puzzle1)))
    start_puzzle2 = int(round(time.time() * 1000))
    res_puzzle2 = puzzle2()
    end_puzzle2 = int(round(time.time() * 1000))
    print("Puzzle 2: " + str(res_puzzle2) + ". Took: " + str((end_puzzle2 - start_puzzle2)))
