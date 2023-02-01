import time

vowels = "aeiou"
naughties = ["ab", "cd", "pq", "xy"]


def puzzle1():
    res = 0
    for string in open('day5.txt').read().split("\n"):
        if any(naughty in string for naughty in naughties):
            continue
        vowelcount = 0
        for vowel in vowels:
            vowelcount += string.count(vowel)
        double = False
        for i in range(len(string) - 1):
            if string[i] == string[i + 1]:
                double = True
        if vowelcount >= 3 and double:
            res += 1
    return res


def puzzle2():
    res = 0
    for string in open('day5.txt').read().split("\n"):
        first = False
        for i in range(len(string) - 3):
            sub = string[i: i + 2]
            if sub in string[i + 2:]:
                first = True
                break
        if not first:
            continue
        second = False
        for i in range(len(string) - 2):
            if string[i] == string[i + 2]:
                second = True
                break
        if second:
            res += 1
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
