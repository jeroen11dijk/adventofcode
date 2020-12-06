import time


def puzzle1():
    res = 0
    with open('day6.txt') as f:
        for line in f.read().split("\n\n"):
            res += len(set([letter for letter in line.replace('\n', '')]))
    return res


def puzzle2():
    res = 0
    with open('day6.txt') as f:
        for line in f.read().split("\n\n"):
            for question in line.split('\n')[0]:
                res += all([question in line for line in line.split('\n')])
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
