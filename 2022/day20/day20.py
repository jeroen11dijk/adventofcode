import time


def puzzle1():
    res = []
    conversion = {}
    for i, line in enumerate(open('day20.txt').read().splitlines()):
        conversion[i] = int(line)
        res.append(i)
    for i in range(len(res)):
        index = res.index(i)
        new_index = (index + conversion[i]) % (len(res) - 1)
        res.remove(res[index])
        res.insert(new_index, i)
    zero_index = [conversion[x] for x in res].index(0)
    return sum([conversion[res[(zero_index + x) % len(res)]] for x in [1000, 2000, 3000]])


def puzzle2():
    res = []
    conversion = {}
    for i, line in enumerate(open('day20.txt').read().splitlines()):
        conversion[i] = int(line)*811589153
        res.append(i)
    for _ in range(10):
        for i in range(len(res)):
            index = res.index(i)
            new_index = (index + conversion[i]) % (len(res) - 1)
            res.remove(res[index])
            res.insert(new_index, i)
    zero_index = [conversion[x] for x in res].index(0)
    return sum([conversion[res[(zero_index + x) % len(res)]] for x in [1000, 2000, 3000]])


if __name__ == '__main__':
    start_puzzle1 = int(round(time.time() * 1000))
    res_puzzle1 = puzzle1()
    end_puzzle1 = int(round(time.time() * 1000))
    print("Puzzle 1: " + str(res_puzzle1) + ". Took: " + str((end_puzzle1 - start_puzzle1)))
    start_puzzle2 = int(round(time.time() * 1000))
    res_puzzle2 = puzzle2()
    end_puzzle2 = int(round(time.time() * 1000))
    print("Puzzle 2: " + str(res_puzzle2) + ". Took: " + str((end_puzzle2 - start_puzzle2)))
