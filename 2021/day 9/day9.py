import time


def checklowpoint(row, column, grid):
    point = grid[row][column]
    neighbours = [point]
    if row - 1 > -1:
        neighbours.append(grid[row - 1][column])
    if row + 1 < len(grid):
        neighbours.append(grid[row + 1][column])
    if column - 1 > -1:
        neighbours.append(grid[row][column - 1])
    if column + 1 < len(grid[row]):
        neighbours.append(grid[row][column + 1])
    if min(neighbours) == point and point != 9:
        return True
    else:
        return False


def puzzle1():
    grid = []
    lowpoints = []
    for i, line in enumerate(open('day9.txt').read().split("\n")):
        grid.append([])
        for value in line:
            grid[i].append(int(value))
    for row in range(len(grid)):
        for column in range(len(grid[row])):
            if checklowpoint(row, column, grid):
                lowpoints.append(grid[row][column])
    return sum(lowpoints) + len(lowpoints)


def checkneighbours(row, column, grid):
    point = grid[row][column]
    if point == 9:
        return set()
    res = {(row, column)}
    if row - 1 > -1 and grid[row - 1][column] > point:
        res = res.union(checkneighbours(row - 1, column, grid))
    if row + 1 < len(grid) and grid[row + 1][column] > point:
        res = res.union(checkneighbours(row + 1, column, grid))
    if column - 1 > -1 and grid[row][column - 1] > point:
        res = res.union(checkneighbours(row, column - 1, grid))
    if column + 1 < len(grid[row]) and grid[row][column + 1] > point:
        res = res.union(checkneighbours(row, column + 1, grid))
    return res


def puzzle2():
    grid = []
    lowpoints = []
    for i, line in enumerate(open('day9.txt').read().split("\n")):
        grid.append([])
        for value in line:
            grid[i].append(int(value))
    for row in range(len(grid)):
        for column in range(len(grid[row])):
            if checklowpoint(row, column, grid):
                lowpoints.append(len(checkneighbours(row, column, grid)))
    lowpoints = sorted(lowpoints, reverse=True)
    print(lowpoints)
    return lowpoints[0] * lowpoints[1] * lowpoints[2]


if __name__ == '__main__':
    start_puzzle1 = int(round(time.time() * 1000))
    res_puzzle1 = puzzle1()
    end_puzzle1 = int(round(time.time() * 1000))
    print("Puzzle 1: " + str(res_puzzle1) + ". Took: " + str((end_puzzle1 - start_puzzle1)))
    start_puzzle2 = int(round(time.time() * 1000))
    res_puzzle2 = puzzle2()
    end_puzzle2 = int(round(time.time() * 1000))
    print("Puzzle 2: " + str(res_puzzle2) + ". Took: " + str((end_puzzle2 - start_puzzle2)))
