import re
import time


def solve1(expression):
    res = 0
    add = True
    in_bracket = False
    bracket = []
    open = 0
    for x in expression:
        if in_bracket:
            if ")" in x:
                open -= x.count(")")
                if open == 0:
                    bracket.append(x.replace(")", "", 1))
                    res = res + solve1(bracket) if add else res * solve1(bracket)
                    in_bracket = False
                    bracket = []
                else:
                    bracket.append(x)
            else:
                open += x.count("(")
                bracket.append(x)
        else:
            if x == "+":
                add = True
            elif x == "*":
                add = False
            elif "(" in x:
                in_bracket = True
                open = x.count("(")
                bracket.append(x.replace("(", "", 1))
            else:
                res = res + int(x) if add else res * int(x)
    return res


def puzzle1():
    res = 0
    for line in open("day18.txt"):
        res += solve1(line.split())
    return res


class Num(int):
    def __mul__(self, b):
        return Num(int(self) + b)

    def __add__(self, b):
        return Num(int(self) + b)

    def __sub__(self, b):
        return Num(int(self) * b)


def puzzle2():
    res = 0
    for line in open("day18.txt"):
        line = re.sub(r"(\d+)", r"Num(\1)", line)
        line = line.replace("*", "-")
        line = line.replace("+", "*")
        res += eval(line, {}, {"Num": Num})
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
