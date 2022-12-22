import re
import time
import numpy as np

def puzzle1():
    grid = []
    graph = {}
    gridlines, instruction = open("day22.txt").read().split("\n\n")
    width = 0
    start = (gridlines.split('\n')[0].index('.')+1,1)
    for line in gridlines.split('\n'):
        grid.append([val for val in line])
        width = max(width, len(line))
    for row in grid:
        if len(row) < width:
            row += [' '] * (width - len(row))
    trans = np.array(grid, dtype=object).T.tolist()
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            nbr = []
            current = grid[y][x]
            leftindex = grid[y].index('.')
            if '#' in grid[y]:
                leftindex = min(leftindex, grid[y].index('#'))
            rightindex = max(loc for loc, val in enumerate(grid[y]) if val == '.' or val == '#')
            lowerindex = trans[x].index('.')
            if '#' in trans[x]:
                lowerindex = min(lowerindex, trans[x].index('#'))
            upperindex = max(loc for loc, val in enumerate(trans[x]) if val == '.' or val == '#')
            if current == '.':
                # Right
                if x+1 <= rightindex and grid[y][x+1] == '.':
                    nbr.append((x+2, y+1))
                elif x+1 > rightindex and grid[y][leftindex] == ".":
                    nbr.append((leftindex+1, y+1))
                else:
                    nbr.append((x+1, y+1))
                # Below
                if y+1 <= upperindex and grid[y+1][x] == '.':
                    nbr.append((x+1, y+2))
                elif y+1 > upperindex and grid[lowerindex][x] == ".":
                    nbr.append((x+1, lowerindex+1))
                else:
                    nbr.append((x+1, y+1))
                # Left
                if x-1 >= leftindex and grid[y][x-1] == '.':
                    nbr.append((x, y+1))
                elif x-1 < leftindex and grid[y][rightindex] == ".":
                    nbr.append((rightindex + 1, y+1))
                else:
                    nbr.append((x+1, y+1))
                # Above
                if y-1 >= lowerindex and grid[y-1][x] == '.':
                    nbr.append((x+1, y))
                elif y-1 < lowerindex and grid[upperindex][x] == ".":
                    nbr.append((x+1, upperindex+1))
                else:
                    nbr.append((x+1, y+1))
                graph[(x+1, y+1)] = nbr
    direction = 0
    current = start
    for steps, rotation in zip([int(x) for x in re.findall("\d+", instruction)], [x for x in re.findall("[A-Z]+", instruction)]):
        for _ in range(steps):
            current = graph[current][direction]
        direction += 1 if rotation == "R" else -1
        direction = direction % 4
    return 1000*current[1] + 4*current[0] + direction








def puzzle2():
    return None


if __name__ == '__main__':
    start_puzzle1 = int(round(time.time() * 1000))
    res_puzzle1 = puzzle1()
    end_puzzle1 = int(round(time.time() * 1000))
    print("Puzzle 1: " + str(res_puzzle1) + ". Took: " + str((end_puzzle1 - start_puzzle1)))
    start_puzzle2 = int(round(time.time() * 1000))
    res_puzzle2 = puzzle2()
    end_puzzle2 = int(round(time.time() * 1000))
    print("Puzzle 2: " + str(res_puzzle2) + ". Took: " + str((end_puzzle2 - start_puzzle2)))
