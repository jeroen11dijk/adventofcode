import itertools
import time


def flash(row, col, grid, flashes):
    flashes += 1
    grid[row][col] = 101
    for i in range(-1, 2):
        for j in range(-1, 2):
            if -1 < row + i < len(grid) and -1 < col + j < len(grid[0]):
                if grid[row + i][col + j] == 9:
                    grid, flashes = flash(row + i, col + j, grid, flashes)
                grid[row + i][col + j] += 1
    return grid, flashes


def puzzle1():
    grid = []
    res = 0
    for i, line in enumerate(open('day11.txt').read().split("\n")):
        grid.append([])
        for value in line:
            grid[i].append(int(value))
    for _ in range(100):
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 9:
                    grid, res = flash(row, col, grid, res)
                grid[row][col] += 1
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] > 100:
                    grid[row][col] = 0
    return res


def puzzle2():
    grid = []
    res = 1
    for i, line in enumerate(open('day11.txt').read().split("\n")):
        grid.append([])
        for value in line:
            grid[i].append(int(value))
    while True:
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 9:
                    grid, _ = flash(row, col, grid, 0)
                grid[row][col] += 1
        if all(x > 100 for x in itertools.chain(*grid)):
            return res
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] > 100:
                    grid[row][col] = 0
        res += 1


if __name__ == '__main__':
    start_puzzle1 = int(round(time.time() * 1000))
    res_puzzle1 = puzzle1()
    end_puzzle1 = int(round(time.time() * 1000))
    print("Puzzle 1: " + str(res_puzzle1) + ". Took: " + str((end_puzzle1 - start_puzzle1)))
    start_puzzle2 = int(round(time.time() * 1000))
    res_puzzle2 = puzzle2()
    end_puzzle2 = int(round(time.time() * 1000))
    print("Puzzle 2: " + str(res_puzzle2) + ". Took: " + str((end_puzzle2 - start_puzzle2)))
