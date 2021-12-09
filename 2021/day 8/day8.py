import itertools
import time


def puzzle1():
    res = 0
    for line in open('day8.txt').readlines():
        _, relevant = line.split("|")
        relevant = relevant.split()
        for value in relevant:
            if len(value) == 2 or len(value) == 3 or len(value) == 4 or len(value) == 7:
                res += 1
    return res


correct = {"abcefg": 0, "cf": 1, "acdeg": 2, "acdfg": 3, "bcdf": 4, "abdfg": 5, "abdefg": 6, "acf": 7, "abcdefg": 8,
           "abcdfg": 9}


def check(long, perm):
    lookup = {perm[0]: "a", perm[1]: "b", perm[2]: "c", perm[3]: "d", perm[4]: "e", perm[5]: "f", perm[6]: "g"}
    for value in long.split():
        string = ""
        for i in value:
            string += lookup[i]
        string = ''.join(sorted(string))
        if string not in correct:
            return False
    return True


def convert(short, perm):
    res = ""
    lookup = {perm[0]: "a", perm[1]: "b", perm[2]: "c", perm[3]: "d", perm[4]: "e", perm[5]: "f", perm[6]: "g"}
    for value in short.split():
        string = ""
        for i in value:
            string += lookup[i]
        string = ''.join(sorted(string))
        res += str(correct[string])
    return res


def puzzle2():
    res = []
    for line in open('day8.txt').readlines():
        long, short = line.split("|")
        for perm in itertools.permutations("abcdefg"):
            if check(long, perm):
                res.append(int(convert(short, perm)))
    return sum(res)


if __name__ == '__main__':
    start_puzzle1 = int(round(time.time() * 1000))
    res_puzzle1 = puzzle1()
    end_puzzle1 = int(round(time.time() * 1000))
    print("Puzzle 1: " + str(res_puzzle1) + ". Took: " + str((end_puzzle1 - start_puzzle1)))
    start_puzzle2 = int(round(time.time() * 1000))
    res_puzzle2 = puzzle2()
    end_puzzle2 = int(round(time.time() * 1000))
    print("Puzzle 2: " + str(res_puzzle2) + ". Took: " + str((end_puzzle2 - start_puzzle2)))
