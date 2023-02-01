import time


def puzzle1():
    res = 0
    with open('day3.txt') as f:
        f.__next__()
        for i, line in enumerate(f , 1):
            res += line[(i * 3) % (len(line.strip('\n')))] == '#'
    return res


def puzzle2():
    res = 5 * [0]
    with open('day3.txt') as f:
        f.__next__()
        for i, line in enumerate(f, 1):
            res[0] += line[i % (len(line.strip('\n')))] == '#'
            res[1] += line[(i * 3) % (len(line.strip('\n')))] == '#'
            res[2] += line[(i * 5) % (len(line.strip('\n')))] == '#'
            res[3] += line[(i * 7) % (len(line.strip('\n')))] == '#'
            if i % 2 == 1:
                res[4] += line[int(i + 1/2) % (len(line.strip('\n')))] == '#'
    return res[0] * res[1] * res[2] * res[3] * res[4]


if __name__ == '__main__':
    start_puzzle1 = int(round(time.time() * 1000))
    res_puzzle1 = puzzle1()
    end_puzzle1 = int(round(time.time() * 1000))
    print("Puzzle 1: " + str(res_puzzle1) + ". Took: " + str((end_puzzle1 - start_puzzle1)))
    start_puzzle2 = int(round(time.time() * 1000))
    res_puzzle2 = puzzle2()
    end_puzzle2 = int(round(time.time() * 1000))
    print("Puzzle 2: " + str(res_puzzle2) + ". Took: " + str((end_puzzle2 - start_puzzle2)))
