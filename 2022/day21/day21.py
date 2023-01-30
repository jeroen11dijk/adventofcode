import re
import time


def get_value(key, instructions):
    if isinstance(instructions[key], int) or isinstance(instructions[key], complex):
        return instructions[key]
    operator = re.search("[*+-/]+", instructions[key]).group(0)
    var = [str(get_value(x, instructions)) for x in re.findall("[a-z]+", instructions[key])]
    return eval(str(var[0] + operator + var[1]))


def puzzle1():
    instructions = {}
    for line in open('day21.txt').read().splitlines():
        key = line.split(": ")[0]
        value = line.split(": ")[1]
        if value.isdigit():
            instructions[key] = int(value)
        else:
            instructions[key] = value
    return get_value("root", instructions)


def puzzle2():
    instructions = {}
    for line in open('day21.txt').read().splitlines():
        key = line.split(": ")[0]
        value = line.split(": ")[1]
        if value.isdigit():
            instructions[key] = int(value)
        else:
            instructions[key] = value
    instructions["humn"] = 1j
    a, b = [get_value(x, instructions) for x in re.findall("[a-z]+", instructions["root"])]
    return round((b - a.real) / a.imag)


if __name__ == '__main__':
    start_puzzle1 = int(round(time.time() * 1000))
    res_puzzle1 = puzzle1()
    end_puzzle1 = int(round(time.time() * 1000))
    print("Puzzle 1: " + str(res_puzzle1) + ". Took: " + str((end_puzzle1 - start_puzzle1)))
    start_puzzle2 = int(round(time.time() * 1000))
    res_puzzle2 = puzzle2()
    end_puzzle2 = int(round(time.time() * 1000))
    print("Puzzle 2: " + str(res_puzzle2) + ". Took: " + str((end_puzzle2 - start_puzzle2)))
