import time


def puzzle1():
    res = 0
    for line in open('day3.txt').readlines():
        a, b = line[:len(line) // 2], line[len(line) // 2:]
        common = "".join(set(a).intersection(set(b)))
        res += ord(common) - 96 if common.islower() else ord(common.lower()) - 70
    return res


def puzzle2():
    res = 0
    with open('day3.txt') as f:
        lines = f.read().splitlines()
        for i in range(0, len(lines), 3):
            line1, line2, line3 = lines[i:i + 3]
            common = "".join(set(line1).intersection(set(line2)).intersection(set(line3)))
            res += ord(common) - 96 if common.islower() else ord(common.lower()) - 70
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
