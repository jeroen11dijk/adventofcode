import time


def puzzle1():
    res = 0
    for line in open('day4.txt').read().splitlines():
        a, b = line.split(",")
        seta = set([i for i in range(int(a.split("-")[0]), int(a.split("-")[1]) + 1)])
        setb = set([i for i in range(int(b.split("-")[0]), int(b.split("-")[1]) + 1)])
        if seta.issubset(setb) or setb.issubset(seta):
            res += 1
    return res


def puzzle2():
    res = 0
    for line in open('day4.txt').read().splitlines():
        a, b = line.split(",")
        seta = set([i for i in range(int(a.split("-")[0]), int(a.split("-")[1]) + 1)])
        setb = set([i for i in range(int(b.split("-")[0]), int(b.split("-")[1]) + 1)])
        if seta.intersection(setb) != set() or setb.intersection(seta) != set():
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
