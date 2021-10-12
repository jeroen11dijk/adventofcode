import time

from lark.exceptions import LarkError
from lark.lark import Lark


def puzzle1():
    rules, lines = open("day19.txt").read().split('\n\n')
    rules = rules.translate(str.maketrans('0123456789', 'abcdefghij'))
    parser = Lark(rules, start='a')

    total = 0
    for line in lines.splitlines():
        try:
            parser.parse(line)
            total += 1
        except LarkError:
            pass
    return total


def puzzle2():
    rules, lines = open("day19.txt").read().split('\n\n')
    rules = rules.replace('8: 42', '8: 42 | 42 8')
    rules = rules.replace('11: 42 31', '11: 42 31 | 42 11 31')
    rules = rules.translate(str.maketrans('0123456789', 'abcdefghij'))
    parser = Lark(rules, start='a')

    total = 0
    for line in lines.splitlines():
        try:
            parser.parse(line)
            total += 1
        except LarkError:
            pass
    return total


if __name__ == '__main__':
    start_puzzle1 = int(round(time.time() * 1000))
    res_puzzle1 = puzzle1()
    end_puzzle1 = int(round(time.time() * 1000))
    print("Puzzle 1: " + str(res_puzzle1) + ". Took: " + str((end_puzzle1 - start_puzzle1)))
    start_puzzle2 = int(round(time.time() * 1000))
    res_puzzle2 = puzzle2()
    end_puzzle2 = int(round(time.time() * 1000))
    print("Puzzle 2: " + str(res_puzzle2) + ". Took: " + str((end_puzzle2 - start_puzzle2)))
