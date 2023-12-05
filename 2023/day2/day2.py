import time


def puzzle1():
    res = 0
    for line in open("day2.txt").splitlines():
        first, second = "0", "0"
        for i in line:
            if i.isdigit():
                first = i
                break
        for i in reversed(line):
            if i.isdigit():
                second = i
                break
        res += int(first + second)
    return res


def puzzle2():
    res = 0
    digits = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    for line in open("day2.txt").read().split("\n"):
        first, second = "0", "0"
        first_index, second_index = len(line) - 1, 0
        for i, val in enumerate(line):
            if val.isdigit():
                first = val
                first_index = i
                break
        for i, val in enumerate(reversed(line)):
            if val.isdigit():
                second = val
                second_index = len(line) - 1 - i
                break
        for string_digit, digit in digits.items():
            index = line.find(string_digit)
            if index != -1 and index < first_index:
                first = digit
                first_index = index
            index = line.rfind(string_digit)
            if index > second_index:
                second = digit
                second_index = index
        print(line, first, second)
        res += int(first + second)
    return res


if __name__ == "__main__":
    start_puzzle1 = int(round(time.time() * 1000))
    res_puzzle1 = puzzle1()
    end_puzzle1 = int(round(time.time() * 1000))
    print(
        "Puzzle 1: "
        + str(res_puzzle1)
        + ". Took: "
        + str((end_puzzle1 - start_puzzle1))
    )
    start_puzzle2 = int(round(time.time() * 1000))
    res_puzzle2 = puzzle2()
    end_puzzle2 = int(round(time.time() * 1000))
    print(
        "Puzzle 2: "
        + str(res_puzzle2)
        + ". Took: "
        + str((end_puzzle2 - start_puzzle2))
    )
