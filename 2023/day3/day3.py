import time
import re
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def check_left(grid, i, j):
    left_number = ""
    j -= 1
    while j > -1 and grid[i][j].isdigit() and i > -1:
        left_number += grid[i][j]
        j -= 1
    return left_number[::-1]


def check_right(grid, i, j):
    right_number = ""
    j += 1
    while j < len(grid[0]) and grid[i][j].isdigit():
        right_number += grid[i][j]
        j += 1
    return right_number


def add_number_to_res(res, number):
    if number == "":
        return res
    print(res, number)
    return res + int(number)


def get_numbers(grid, i, j):
    numbers = []
    numbers.append(check_right(grid, i, j))
    numbers.append(check_left(grid, i, j))

    bottom_right_number = check_right(grid, i + 1, j)
    bottom_left_number = check_left(grid, i + 1, j)
    if grid[i + 1][j].isdigit():
        bottom_number = bottom_left_number + grid[i + 1][j] + bottom_right_number
        numbers.append(bottom_number)
    else:
        numbers.append(bottom_right_number)
        numbers.append(bottom_left_number)

    top_right_number = check_right(grid, i - 1, j)
    top_left_number = check_left(grid, i - 1, j)
    if grid[i - 1][j].isdigit():
        top_number = top_left_number + grid[i - 1][j] + top_right_number
        numbers.append(top_number)
    else:
        numbers.append(top_right_number)
        numbers.append(top_left_number)
    return numbers


def puzzle1():
    res = 0
    symbols = []
    grid = []
    for i, line in enumerate(open("day3.txt").readlines()):
        grid.append([])
        for j, val in enumerate(line.strip()):
            grid[i].append(val)
            if val != "." and not val.isdigit():
                symbols.append((i, j))
    for symbol in symbols:
        i, j = symbol
        numbers = get_numbers(grid, i, j)
        for number in numbers:
            res = add_number_to_res(res, number)
    return res


def puzzle2():
    res = 0
    symbols = []
    grid = []
    for i, line in enumerate(open("day3.txt").readlines()):
        grid.append([])
        for j, val in enumerate(line.strip()):
            grid[i].append(val)
            if val == "*":
                symbols.append((i, j))
    for symbol in symbols:
        i, j = symbol
        numbers = get_numbers(grid, i, j)
        numbers = [number for number in numbers if number != ""]
        if len(numbers) == 2:
            res += int(numbers[0]) * int(numbers[1])
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
