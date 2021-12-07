import time


def puzzle1():
    data = [int(i) for i in open('day7.txt').read().split("\n\n")[0].split(",")]
    return min(sum([abs(i - j) for j in data]) for i in data)


def puzzle2():
    data = [int(i) for i in open('day7.txt').read().split("\n\n")[0].split(",")]
    return min(sum([abs(i - j)*(abs(i - j)+1) // 2 for j in data]) for i in data)


if __name__ == '__main__':
    start_puzzle1 = int(round(time.time() * 1000))
    res_puzzle1 = puzzle1()
    end_puzzle1 = int(round(time.time() * 1000))
    print("Puzzle 1: " + str(res_puzzle1) + ". Took: " + str((end_puzzle1 - start_puzzle1)))
    start_puzzle2 = int(round(time.time() * 1000))
    res_puzzle2 = puzzle2()
    end_puzzle2 = int(round(time.time() * 1000))
    print("Puzzle 2: " + str(res_puzzle2) + ". Took: " + str((end_puzzle2 - start_puzzle2)))
