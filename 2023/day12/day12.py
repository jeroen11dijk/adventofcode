import time
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def is_valid(line, validator):
    streak = 0
    for i, val in enumerate(line):
        if val == "#":
            streak += 1
        if val != "#" or i == len(line) - 1:
            if streak == 0:
                streak = 0
                continue
            if len(validator) == 0 or streak != validator[0]:
                return False
            streak = 0
            validator.pop(0)         
    return len(validator) == 0
            
        

def puzzle1():
    res = 0
    for line in open("day12.txt").read().splitlines():
        weird_shit, numbers = line.split()
        numbers = [int(val) for val in numbers.split(",")]
        all_possibilities = [[]]
        for val in weird_shit:
            new = []
            if val != "?":
                for possibility in all_possibilities:
                    new.append(possibility + [val])
            else:
                for possibility in all_possibilities:
                    new.append(possibility + ["."])
                    new.append(possibility + ["#"])
            all_possibilities = new
        for possibility in all_possibilities:
            valid = is_valid(possibility, numbers)
            res += valid
    return res


def puzzle2():
    return 0


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
