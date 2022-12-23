import time


def puzzle1():
    grid = set()
    for i, line in enumerate(open('day23.txt').read().splitlines()):
        for j, val in enumerate(line):
            if val == "#":
                grid.add((j, i))
    index = 0
    directions = {0: [(0, -1), (1, -1), (-1, -1)], 1: [(0, 1), (1, 1), (-1, 1)], 2: [(-1, 0), (-1, 1), (-1, -1)],
                  3: [(1, 0), (1, 1), (1, -1)]}
    for _ in range(10):
        proposals = {}
        for current in list(grid):
            if all([(current[0] + x, current[1] + y) not in grid for x in [-1, 0, 1] for y in [-1, 0, 1] if
                    x != 0 or y != 0]):
                proposals[current] = current
            else:
                for i in range(index, index + 4):
                    i = i % 4
                    dir = directions[i]
                    check1 = (current[0] + dir[0][0], current[1] + dir[0][1]) not in grid
                    check2 = (current[0] + dir[1][0], current[1] + dir[1][1]) not in grid
                    check3 = (current[0] + dir[2][0], current[1] + dir[2][1]) not in grid
                    if check1 and check2 and check3:
                        proposals[current] = current[0] + dir[0][0], current[1] + dir[0][1]
                        break
                    if i == (index + 3) % 4:
                        proposals[current] = current
        new_grid = set()
        for key in proposals:
            if list(proposals.values()).count(proposals[key]) > 1:
                new_grid.add(key)
            else:
                new_grid.add(proposals[key])
        grid = new_grid
        index += 1
    minx, maxx, miny, maxy = float("inf"), 0, float("inf"), 0
    for current in list(grid):
        minx, maxx, miny, maxy = min(minx, current[0]), max(maxx, current[0]), min(miny, current[1]), max(maxy,
                                                                                                          current[1])
    res = 0
    for x in range(minx, maxx + 1):
        for y in range(miny, maxy + 1):
            res += (x, y) not in grid
    return res


def puzzle2():
    grid = set()
    for i, line in enumerate(open('day23.txt').read().splitlines()):
        for j, val in enumerate(line):
            if val == "#":
                grid.add((j, i))
    index = 0
    directions = {0: [(0, -1), (1, -1), (-1, -1)], 1: [(0, 1), (1, 1), (-1, 1)], 2: [(-1, 0), (-1, 1), (-1, -1)],
                  3: [(1, 0), (1, 1), (1, -1)]}
    steps = 1
    while True:
        print(steps)
        proposals = {}
        for current in list(grid):
            if all([(current[0] + x, current[1] + y) not in grid for x in [-1, 0, 1] for y in [-1, 0, 1] if
                    x != 0 or y != 0]):
                proposals[current] = current
            else:
                for i in range(index, index + 4):
                    i = i % 4
                    dir = directions[i]
                    check1 = (current[0] + dir[0][0], current[1] + dir[0][1]) not in grid
                    check2 = (current[0] + dir[1][0], current[1] + dir[1][1]) not in grid
                    check3 = (current[0] + dir[2][0], current[1] + dir[2][1]) not in grid
                    if check1 and check2 and check3:
                        proposals[current] = current[0] + dir[0][0], current[1] + dir[0][1]
                        break
                    if i == (index + 3) % 4:
                        proposals[current] = current
        new_grid = set()
        for key in proposals:
            if list(proposals.values()).count(proposals[key]) > 1:
                new_grid.add(key)
            else:
                new_grid.add(proposals[key])
        if grid == new_grid:
            return steps
        grid = new_grid
        index += 1
        steps += 1


if __name__ == '__main__':
    start_puzzle1 = int(round(time.time() * 1000))
    res_puzzle1 = puzzle1()
    end_puzzle1 = int(round(time.time() * 1000))
    print("Puzzle 1: " + str(res_puzzle1) + ". Took: " + str((end_puzzle1 - start_puzzle1)))
    start_puzzle2 = int(round(time.time() * 1000))
    res_puzzle2 = puzzle2()
    end_puzzle2 = int(round(time.time() * 1000))
    print("Puzzle 2: " + str(res_puzzle2) + ". Took: " + str((end_puzzle2 - start_puzzle2)))
