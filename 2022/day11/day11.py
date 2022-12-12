import re
import time
import numpy as np

class Monkey:

    def __init__(self, items, operation, divide, true, false):
        self.items = items
        self.operation = operation
        self.divide = divide
        self.true = true
        self.false = false
        self.throws = 0

def parse_input():
    monkeys = []
    for line in open('day11.txt').read().split("\n\n"):
        items = [int(x) for x in re.findall('[0-9]+', line.split("\n")[1])]
        operation = re.findall('\= (.*)', line.split("\n")[2])[0]
        divide = int(re.search('[0-9]+', line.split("\n")[3]).group(0))
        true = int(re.search('[0-9]+', line.split("\n")[4]).group(0))
        false = int(re.search('[0-9]+', line.split("\n")[5]).group(0))
        monkeys.append(Monkey(items, operation, divide, true, false))
    return monkeys


def puzzle1():
    monkeys = parse_input()
    for _ in range(20):
        for monkey in monkeys:
            for item in monkey.items:
                worry = int(eval(monkey.operation.replace("old", str(item))) / 3)
                if worry % monkey.divide == 0:
                    monkeys[monkey.true].items.append(worry)
                else:
                    monkeys[monkey.false].items.append(worry)
                monkey.throws += 1
            monkey.items = []
    throws = sorted([monkey.throws for monkey in monkeys], reverse=True)
    return throws[0] * throws[1]


def puzzle2():
    monkeys = parse_input()
    group = np.product([monkey.divide for monkey in monkeys])
    for _ in range(10000):
        for monkey in monkeys:
            for item in monkey.items:
                worry = eval(monkey.operation.replace("old", str(item))) % group
                if worry % monkey.divide == 0:
                    monkeys[monkey.true].items.append(worry)
                else:
                    monkeys[monkey.false].items.append(worry)
                monkey.throws += 1
            monkey.items = []
    throws = sorted([monkey.throws for monkey in monkeys], reverse=True)
    return throws[0] * throws[1]


if __name__ == '__main__':
    start_puzzle1 = int(round(time.time() * 1000))
    res_puzzle1 = puzzle1()
    end_puzzle1 = int(round(time.time() * 1000))
    print("Puzzle 1: " + str(res_puzzle1) + ". Took: " + str((end_puzzle1 - start_puzzle1)))
    start_puzzle2 = int(round(time.time() * 1000))
    res_puzzle2 = puzzle2()
    end_puzzle2 = int(round(time.time() * 1000))
    print("Puzzle 2: " + str(res_puzzle2) + ". Took: " + str((end_puzzle2 - start_puzzle2)))
