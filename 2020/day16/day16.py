import math
import time
from collections import defaultdict


def puzzle1():
    parts = open("day16.txt").read().split("\n\n")
    valid = set()
    for line in parts[0].split("\n"):
        for span in line.split(': ')[1].split(' or '):
            for i in range(int(span.split("-")[0]), int(span.split("-")[1]) + 1):
                valid.add(i)
    return sum([sum([i if i not in valid else 0 for i in list(map(int, line.split(",")))]) for line in parts[2].split("\n")[1:]])


def invalid_lines():
    valid = set()
    res = []
    parts = open("day16.txt").read().split("\n\n")
    for line in parts[0].split("\n"):
        for span in line.split(': ')[1].split(' or '):
            for i in range(int(span.split("-")[0]), int(span.split("-")[1]) + 1):
                valid.add(i)
    for line in parts[2].split("\n")[1:]:
        for i in list(map(int, line.split(","))):
            if i not in valid:
                res.append(list(map(int, line.split(","))))
    return res


def puzzle2():
    parts = open("day16.txt").read().split("\n\n")
    valid_per_field = defaultdict(set)
    valid = set()
    # Get all the valid numbers for every field
    for line in parts[0].split("\n"):
        field, ranges = line.split(': ')
        for span in ranges.split(' or '):
            for i in range(int(span.split("-")[0]), int(span.split("-")[1]) + 1):
                valid_per_field[field].add(i)
                valid.add(i)
    values_per_column = [set() for _ in range(len(parts[2].split("\n")[1].split(",")))]
    for line in parts[2].split("\n")[1:]:
        line = list(map(int, line.split(",")))
        if all([value in valid for value in line]):
            for i, value in enumerate(line):
                values_per_column[i].add(value)
    assigned = set()
    possibilities = defaultdict(list)
    for index, column in enumerate(values_per_column):
        for key in valid_per_field.keys():
            if all(value in valid_per_field[key] for value in column) and key not in assigned:
                possibilities[index].append(key)
        if len(possibilities[index]) == 1:
            assigned.add(possibilities[index][0])
    while not all([len(possibilities[key]) == 1 for key in possibilities.keys()]):
        for key in possibilities.keys():
            if len(possibilities[key]) != 1:
                for value in possibilities[key]:
                    if value in assigned:
                        possibilities[key].remove(value)
            if len(possibilities[key]) == 1:
                assigned.add(possibilities[key][0])
    my_ticket = list(map(int, parts[1].split("\n")[1].split(",")))
    interested_in = ["departure location", "departure station", "departure platform", "departure track",
                     "departure date", "departure time"]
    return math.prod([my_ticket[index] if possibilities[index][0] in interested_in else 1 for index in range(len(my_ticket))])


if __name__ == '__main__':
    start_puzzle1 = int(round(time.time() * 1000))
    res_puzzle1 = puzzle1()
    end_puzzle1 = int(round(time.time() * 1000))
    print("Puzzle 1: " + str(res_puzzle1) + ". Took: " + str((end_puzzle1 - start_puzzle1)))
    start_puzzle2 = int(round(time.time() * 1000))
    res_puzzle2 = puzzle2()
    end_puzzle2 = int(round(time.time() * 1000))
    print("Puzzle 2: " + str(res_puzzle2) + ". Took: " + str((end_puzzle2 - start_puzzle2)))