import itertools
import time


def puzzle1():
    grid = []
    for i, line in enumerate(open('day8.txt').read().splitlines()):
        grid.append([int(val) for val in line])
    transpose = list(map(list, zip(*grid)))
    res = len(grid) * 2 + (len(grid) - 2) * 2
    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid) - 1):
            val = grid[i][j]
            edge = len(grid)
            neighbours = [max(transpose[j][i + 1:edge]), max(transpose[j][0:i]), max(grid[i][j + 1:edge]),
                          max(grid[i][0:j])]
            if val > min(neighbours):
                res += 1
    return res


def sight_dir(val, direction):
    res = 0
    for nbr in direction:
        if val > nbr:
            res += 1
        else:
            res += 1
            break
    return res


def puzzle2():
    res = 0
    grid = []
    for i, line in enumerate(open('day8.txt').read().splitlines()):
        grid.append([int(val) for val in line])
    transpose = list(map(list, zip(*grid)))
    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid) - 1):
            val = grid[i][j]
            edge = len(grid)
            down = sight_dir(val, transpose[j][i + 1:edge])
            up = sight_dir(val, reversed(transpose[j][0:i]))
            left = sight_dir(val, grid[i][j + 1:edge])
            right = sight_dir(val, reversed(grid[i][0:j]))
            res = max(res, left * right * up * down)
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
