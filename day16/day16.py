import time
from collections import defaultdict
from copy import copy
import math

def puzzle1():
    valid = set()
    res = 0
    for line in open('ids.txt'):
        if line.split() == "your ticket:":
            break
        _, ranges = line.split(': ')
        first, second = ranges.split(' or ')
        for i in range(int(first.split("-")[0]), int(first.split("-")[1]) + 1):
            valid.add(i)
        for i in range(int(second.split("-")[0]), int(second.split("-")[1]) + 1):
            valid.add(i)
    for line in open("day16.txt"):
        line = list(map(int, line.split(",")))
        for i in line:
            if i not in valid:
                res += i
    return res

def invalid_lines():
    valid = set()
    res = []
    for line in open('ids.txt'):
        if line.split() == "your ticket:":
            break
        _, ranges = line.split(': ')
        first, second = ranges.split(' or ')
        for i in range(int(first.split("-")[0]), int(first.split("-")[1]) + 1):
            valid.add(i)
        for i in range(int(second.split("-")[0]), int(second.split("-")[1]) + 1):
            valid.add(i)
    for line_number, line in enumerate(open("day16.txt")):
        line = list(map(int, line.split(",")))
        for i in line:
            if i not in valid:
                res.append(line)
    return res

def puzzle2():
    valid = {}
    skip = invalid_lines()
    for line in open('ids.txt'):
        if line.split() == "your ticket:":
            break
        field, ranges = line.split(': ')
        first, second = ranges.split(' or ')
        valid[field] = set()
        for i in range(int(first.split("-")[0]), int(first.split("-")[1]) + 1):
            valid[field].add(i)
        for i in range(int(second.split("-")[0]), int(second.split("-")[1]) + 1):
            valid[field].add(i)
    lijsten = []
    for i in range(len(open("day16.txt").readlines()[0].split(','))):
        lijsten.append(set())
    for line in open("day16.txt"):
        line = list(map(int, line.split(",")))
        if line not in skip:
            for i, value in enumerate(line):
                lijsten[i].add(value)
    assigned = set()
    possibilities = defaultdict(list)
    for index, lijst in enumerate(lijsten):
        for key in valid.keys():
            if all(value in valid[key] for value in lijst) and key not in assigned:
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
    print(assigned)
    my_ticket = list(map(int, "191,61,149,157,79,197,67,139,59,71,163,53,73,137,167,173,193,151,181,179".split(",")))
    interested_in = ["departure location", "departure station", "departure platform", "departure track", "departure date", "departure time"]
    res = []
    for index in range(len(my_ticket)):
        if possibilities[index][0] in interested_in:
            res.append(my_ticket[index])
    return math.prod(res)


if __name__ == '__main__':
    start_puzzle1 = int(round(time.time() * 1000))
    res_puzzle1 = puzzle1()
    end_puzzle1 = int(round(time.time() * 1000))
    print("Puzzle 1: " + str(res_puzzle1) + ". Took: " + str((end_puzzle1 - start_puzzle1)))
    start_puzzle2 = int(round(time.time() * 1000))
    res_puzzle2 = puzzle2()
    end_puzzle2 = int(round(time.time() * 1000))
    print("Puzzle 2: " + str(res_puzzle2) + ". Took: " + str((end_puzzle2 - start_puzzle2)))
