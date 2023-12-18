import time
import re
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def get_energized(start, grid):
    energized = {(0, 0)}
    seen = set()
    current = start
    while len(current) > 0:
        new_current = []
        for location, direction in current:
            if (location, direction) in seen:
                continue
            seen.add((location, direction))
            if (
                location[0] + direction[0] < 0
                or location[0] + direction[0] > len(grid) - 1
            ):
                continue
            if (
                location[1] + direction[1] < 0
                or location[1] + direction[1] > len(grid[0]) - 1
            ):
                continue
            nbr = (location[0] + direction[0], location[1] + direction[1])
            energized.add(nbr)
            nbr_symbol = grid[nbr[0]][nbr[1]]
            if nbr_symbol == "/" and direction == (1, 0):
                new_direction = (0, -1)
                new_current.append((nbr, new_direction))
            elif nbr_symbol == "/" and direction == (-1, 0):
                new_direction = (0, 1)
                new_current.append((nbr, new_direction))
            elif nbr_symbol == "/" and direction == (0, 1):
                new_direction = (-1, 0)
                new_current.append((nbr, new_direction))
            elif nbr_symbol == "/" and direction == (0, -1):
                new_direction = (1, 0)
                new_current.append((nbr, new_direction))
            elif nbr_symbol == "\\" and direction == (1, 0):
                new_direction = (0, 1)
                new_current.append((nbr, new_direction))
            elif nbr_symbol == "\\" and direction == (-1, 0):
                new_direction = (0, -1)
                new_current.append((nbr, new_direction))
            elif nbr_symbol == "\\" and direction == (0, 1):
                new_direction = (1, 0)
                new_current.append((nbr, new_direction))
            elif nbr_symbol == "\\" and direction == (0, -1):
                new_direction = (-1, 0)
                new_current.append((nbr, new_direction))
            elif nbr_symbol == "|" and (direction == (0, 1) or direction == (0, -1)):
                new_current.append((nbr, (1, 0)))
                new_current.append((nbr, (-1, 0)))
            elif nbr_symbol == "-" and (direction == (1, 0) or direction == (-1, 0)):
                new_current.append((nbr, (0, 1)))
                new_current.append((nbr, (0, -1)))
            else:
                new_current.append((nbr, direction))
        current = new_current
    return len(energized)


def puzzle1():
    grid = []
    for i, line in enumerate(open("day16.txt").readlines()):
        grid.append([])
        for val in line.strip():
            grid[i].append(val)
    return get_energized([((0, -1), (0, 1))], grid)


def puzzle2():
    res = 0
    grid = []
    for i, line in enumerate(open("day16.txt").readlines()):
        grid.append([])
        for val in line.strip():
            grid[i].append(val)
    for i in range(len(grid)):
        res = max(res, get_energized([((i, -1), (0, 1))], grid))
        res = max(res, get_energized([((i, len(grid)), (0, -1))], grid))
    for i in range(len(grid[0])):
        res = max(res, get_energized([((-1, i), (1,0))], grid))
        res = max(res, get_energized([((len(grid[0]), i), (-1,0))], grid))
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
