import time


def puzzle1():
    res = 0
    with open('day2.txt') as f:
        for line in f:
            linesplit = line.split()
            min = int(linesplit[0].split('-')[0])
            max = int(linesplit[0].split('-')[1])
            char = linesplit[1][0]
            password = linesplit[2]
            if min <= password.count(char) <= max:
                res += 1
    return res


def puzzle2():
    res = 0
    with open('day2.txt') as f:
        for line in f:
            linesplit = line.split()
            first = int(linesplit[0].split('-')[0]) - 1
            second = int(linesplit[0].split('-')[1]) - 1
            char = linesplit[1][0]
            password = linesplit[2]
            if password[first] == char and password[second] != char:
                res += 1
            if password[first] != char and password[second] == char:
                res += 1
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
