import time

lookup = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}


def get_score(them, me):
    res = me
    if me == them:
        res += 3
    if me == (them % 3) + 1:
        res += 6
    return res


def puzzle1():
    res = 0
    for line in open('day2.txt').readlines():
        res += get_score(lookup[line.split()[0]], lookup[line.split()[1]])
    return res


def puzzle2():
    res = 0
    for line in open('day2.txt').readlines():
        them, result = lookup[line.split()[0]], lookup[line.split()[1]]
        if result == 1:
            res += get_score(them, 3 if them == 1 else them - 1)
        if result == 2:
            res += get_score(them, them)
        if result == 3:
            res += get_score(them, (them % 3) + 1)
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
