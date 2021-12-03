import time


def puzzle1():
    count = []
    for _ in open('day3.txt').read().split()[0]:
        count.append(0)
    for line in open('day3.txt').read().split():
        for i in range(len(line)):
            if int(line[i]) == 1:
                count[i] = count[i] + 1
    gamma, epsilon = "", ""
    for i in count:
        if i > len(open('day3.txt').read().split()) / 2:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"
    return int(gamma, 2) * int(epsilon, 2)


def find(lst, depth):
    oxygen, co2 = [], []
    left, right = [], []
    for value in lst:
        if int(value[depth]) == 0:
            left.append(value)
        else:
            right.append(value)
        if len(left) > len(right):
            oxygen = left
            co2 = right
        else:
            oxygen = right
            co2 = left
    return oxygen, co2


def puzzle2():
    oxygen, co2 = find(open('day3.txt').read().split(), 0)
    depth = 1
    while len(oxygen) > 1:
        oxygen, _ = find(oxygen, depth)
        depth += 1
    depth = 1
    while len(co2) > 1:
        _, co2 = find(co2, depth)
        depth += 1
    return int(co2[0], 2) * int(oxygen[0], 2)


if __name__ == '__main__':
    start_puzzle1 = int(round(time.time() * 1000))
    res_puzzle1 = puzzle1()
    end_puzzle1 = int(round(time.time() * 1000))
    print("Puzzle 1: " + str(res_puzzle1) + ". Took: " + str((end_puzzle1 - start_puzzle1)))
    start_puzzle2 = int(round(time.time() * 1000))
    res_puzzle2 = puzzle2()
    end_puzzle2 = int(round(time.time() * 1000))
    print("Puzzle 2: " + str(res_puzzle2) + ". Took: " + str((end_puzzle2 - start_puzzle2)))
