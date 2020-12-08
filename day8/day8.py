import time
from copy import copy


def run_commands(lines):
    index = 0
    executed = set()
    acc = 0
    while True:
        if index in executed:
            return False
        if index > len(lines) - 1:
            return acc
        command, value = lines[index].split()
        executed.add(index)
        if command == "nop":
            index += 1
        elif command == "jmp":
            index += int(value)
        else:
            acc += int(value)
            index += 1


def puzzle1():
    lines = open('day8.txt').read().split("\n")
    index = 0
    executed = set()
    acc = 0
    while True:
        if index in executed:
            return acc
        command, value = lines[index].split()
        executed.add(index)
        if command == "nop":
            index += 1
        elif command == "jmp":
            index += int(value)
        else:
            acc += int(value)
            index += 1


def puzzle2():
    original_lines = open('day8.txt').read().split("\n")
    for i in range(0, len(original_lines)):
        lines = original_lines[:]
        if lines[i].startswith("jmp"):
            lines[i] = lines[i].replace("jmp", "nop")
        elif lines[i].startswith("nop"):
            lines[i] = lines[i].replace("nop", "jmp")
        res = run_commands(lines)
        if res:
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
