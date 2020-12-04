import time
import re

eyecolors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

values = {"hgt": lambda x: (x.__contains__("in") and 59 <= int(x.replace("in", "")) <= 76) or (
            x.__contains__("cm") and 150 <= int(x.replace("cm", "")) <= 193), "byr": lambda x: 1920 <= int(x) <= 2002,
          "iyr": lambda x: 2010 <= int(x) <= 2020, "eyr": lambda x: 2020 <= int(x) <= 2030,
          "hcl": lambda x: x[0] == '#' and len(x) == 7 and all(char.isdigit() or ord(char) <= 102 for char in x),
          "ecl": lambda x: eyecolors.__contains__(x),
          "pid": lambda x: len(x) == 9 and all(char.isdigit() for char in x)}


def puzzle1():
    res = 0
    with open('day4.txt') as f:
        lines = f.read().split("\n\n")
        for line in lines:
            res += all(dict(field.split(':') for field in re.split('[\n ]', line)).keys().__contains__(key) for key in values.keys())
    return res


def puzzle2():
    res = 0
    with open('day4.txt') as f:
        lines = f.read().split("\n\n")
        for line in lines:
            passport = dict(field.split(':') for field in re.split('[\n ]', line))
            res += all(passport.keys().__contains__(key) and values[key](passport[key]) for key in values.keys())
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
