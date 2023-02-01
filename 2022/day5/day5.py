import time
import re

def puzzle1():
    data = [["D", "B", "J", "V"],
            ["P", "V", "B", "W", "R", "D", "F"],
            ["R", "G", "F", "L", "D", "C", "W", "Q"],
            ["W", "J", "P", "M", "L", "N", "D", "B"],
            ["H", "N", "B", "P", "C", "S", "Q"],
            ["R", "D", "B", "S", "N", "G"],
            ["Z", "B", "P", "M", "Q", "F", "S", "H"],
            ["W", "L", "F"],
            ["S", "V", "F", "M", "R"]]
    for line in open('day5.txt').read().splitlines():
        move, van, naar = re.findall(r'\d+', line)
        for i in range(1, int(move) + 1):
            data[int(naar) - 1].append(data[int(van) - 1][-i])
        data[int(van) - 1] = data[int(van) - 1][:len(data[int(van) - 1]) - int(move)]
    res = ""
    for stack in data:
        res += stack[-1]
    return res


def puzzle2():
    data = [["D", "B", "J", "V"],
            ["P", "V", "B", "W", "R", "D", "F"],
            ["R", "G", "F", "L", "D", "C", "W", "Q"],
            ["W", "J", "P", "M", "L", "N", "D", "B"],
            ["H", "N", "B", "P", "C", "S", "Q"],
            ["R", "D", "B", "S", "N", "G"],
            ["Z", "B", "P", "M", "Q", "F", "S", "H"],
            ["W", "L", "F"],
            ["S", "V", "F", "M", "R"]]
    for line in open('day5.txt').read().splitlines():
        move, van, naar = re.findall(r'\d+', line)
        data[int(naar) - 1].extend(data[int(van) - 1][-int(move):])
        data[int(van) - 1] = data[int(van) - 1][:len(data[int(van) - 1]) - int(move)]
    res = ""
    for stack in data:
        res += stack[-1]
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
