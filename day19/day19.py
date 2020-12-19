import time

from lark.exceptions import LarkError
from lark.lark import Lark

cache = {}


def hasNoNumbers(input_string):
    if input_string in cache:
        return cache[input_string]
    res = not any(char.isdigit() for char in str(input_string))
    cache[input_string] = res
    return res


def puzzle1():
    res = 0
    parts = open("day19.txt").read().split("\n\n")
    rules = {}
    known = set()
    done = set()
    copycats = set()
    for line in parts[0].split("\n"):
        rule = line.split()
        key = int(rule[0].replace(":", ""))
        if len(rule) == 2:
            if rule[1][1] == "a" or rule[1][1] == "b":
                rules[key] = rule[1][1]
                known.add(key)
                done.add(key)
            else:
                copycats.add(key)
                rules[key] = rule[1]
        else:
            lhs, rhs = [], []
            left = True
            for x in rule[1:]:
                if x == "|":
                    left = False
                    continue
                lhs.append(int(x)) if left else rhs.append(int(x))
                if len(rhs) > 0:
                    rules[key] = [lhs, rhs]
                else:
                    rules[key] = [lhs]
    for copycat in copycats:
        rules[copycat] = rules[int(rules[copycat])]
    while len(known) > 0:
        current_key = known.pop()
        current_values = rules[current_key]
        for key in rules.keys():
            if key != current_key and key not in done:
                new_values = []
                for value in rules[key]:
                    for current_value in current_values:
                        new_value = tuple([current_value if x == current_key else x for x in value])
                        if all(hasNoNumbers(x) for x in new_value):
                            new_value = "".join(new_value)
                        new_values.append(new_value)
                if all([all(hasNoNumbers(x) for x in new_value) for new_value in new_values]):
                    known.add(key)
                    done.add(key)
                rules[key] = list(set(new_values))
    rules_0 = set(rules[0])
    begin = set(rules[29]).union(set(rules[115]))
    for message in parts[1].split("\n"):
        res += message[:7] in begin and len(message) == len(rules_0.pop())
    return res


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
