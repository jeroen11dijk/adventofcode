import time


def step3D(grid):
    new_grid = {}
    min_x = min(key[0] for key in grid.keys()) - 1
    min_y = min(key[1] for key in grid.keys()) - 1
    min_z = min(key[2] for key in grid.keys()) - 1
    max_x = max(key[0] for key in grid.keys()) + 2
    max_y = max(key[1] for key in grid.keys()) + 2
    max_z = max(key[2] for key in grid.keys()) + 2
    for x in range(min_x, max_x):
        for y in range(min_y, max_y):
            for z in range(min_z, max_z):
                active = grid.get((x, y, z), False)
                active_neighbours = 0
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        for dz in range(-1, 2):
                            if dx == dy == dz == 0:
                                continue
                            active_neighbours += grid.get((x + dx, y + dy, z + dz), False)
                if active and active_neighbours != 2 and active_neighbours != 3:
                    new_grid[x, y, z] = 0
                elif not active and active_neighbours == 3:
                    new_grid[x, y, z] = 1
                else:
                    new_grid[x, y, z] = active
    return new_grid


def puzzle1():
    grid = {}
    lines = open("day17.txt").read().split("\n")
    for row, line in enumerate(lines):
        for column, value in enumerate(line):
            grid[row, column, 0] = int(value == "#")
    for i in range(6):
        grid = step3D(grid)
    return sum(grid.values())


def step4D(grid):
    new_grid = {}
    min_x = min(key[0] for key in grid.keys()) - 1
    min_y = min(key[1] for key in grid.keys()) - 1
    min_z = min(key[2] for key in grid.keys()) - 1
    min_w = min(key[3] for key in grid.keys()) - 1
    max_x = max(key[0] for key in grid.keys()) + 2
    max_y = max(key[1] for key in grid.keys()) + 2
    max_z = max(key[2] for key in grid.keys()) + 2
    max_w = max(key[3] for key in grid.keys()) + 2
    for x in range(min_x, max_x):
        for y in range(min_y, max_y):
            for z in range(min_z, max_z):
                for w in range(min_w, max_w):
                    active = grid.get((x, y, z, w), False)
                    active_neighbours = 0
                    for dx in range(-1, 2):
                        for dy in range(-1, 2):
                            for dz in range(-1, 2):
                                for dw in range(-1, 2):
                                    if dx == dy == dz == dw == 0:
                                        continue
                                    active_neighbours += grid.get((x + dx, y + dy, z + dz, w + dw), False)
                    if active and active_neighbours != 2 and active_neighbours != 3:
                        new_grid[x, y, z, w] = 0
                    elif not active and active_neighbours == 3:
                        new_grid[x, y, z, w] = 1
                    else:
                        new_grid[x, y, z, w] = active
    return new_grid


def puzzle2():
    grid = {}
    lines = open("day17.txt").read().split("\n")
    for row, line in enumerate(lines):
        for column, value in enumerate(line):
            grid[row, column, 0, 0] = int(value == "#")
    for i in range(6):
        grid = step4D(grid)
    return sum(grid.values())


if __name__ == '__main__':
    start_puzzle1 = int(round(time.time() * 1000))
    res_puzzle1 = puzzle1()
    end_puzzle1 = int(round(time.time() * 1000))
    print("Puzzle 1: " + str(res_puzzle1) + ". Took: " + str((end_puzzle1 - start_puzzle1)))
    start_puzzle2 = int(round(time.time() * 1000))
    res_puzzle2 = puzzle2()
    end_puzzle2 = int(round(time.time() * 1000))
    print("Puzzle 2: " + str(res_puzzle2) + ". Took: " + str((end_puzzle2 - start_puzzle2)))
