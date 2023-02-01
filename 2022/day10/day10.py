import time


def puzzle1():
    res = 0
    cycle = 1
    X = 1
    for line in open('day10.txt').read().splitlines():
        if (cycle + 20) % 40 == 0:
            res += X * cycle
        cycle += 1
        if line != "noop":
            if (cycle + 20) % 40 == 0:
                res += X * cycle
            X += int(line.split()[1])
            cycle += 1
    return res

def write(X, res):
    if len(res) % 40 == 0 and len(res) > 0 and 40 in [X - 1, X, X + 1]:
        return "#"
    elif len(res) % 40 in [X - 1, X, X + 1]:
        return "#"
    else:
        return "."

def puzzle2():
    res = []
    cycle = 1
    X = 1
    for line in open('day10.txt').read().splitlines():
        res.append(write(X, res))
        cycle += 1
        if line != "noop":
            res.append(write(X, res))
            X += int(line.split()[1])
            cycle += 1
    return [res[i * 40:(i + 1) * 40] for i in range((len(res) + 40 - 1) // 40)]


if __name__ == '__main__':
    start_puzzle1 = int(round(time.time() * 1000))
    res_puzzle1 = puzzle1()
    end_puzzle1 = int(round(time.time() * 1000))
    print("Puzzle 1: " + str(res_puzzle1) + ". Took: " + str((end_puzzle1 - start_puzzle1)))
    start_puzzle2 = int(round(time.time() * 1000))
    res_puzzle2 = puzzle2()
    end_puzzle2 = int(round(time.time() * 1000))
    print("Puzzle 2:")
    for value in res_puzzle2:
        print(value)
    print("Took: " + str((end_puzzle2 - start_puzzle2)))
