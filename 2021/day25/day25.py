import time


def puzzle1():
    grid = {}
    for i, line in enumerate(open('day25.txt').read().splitlines()):
        width = len(line)
        length = len(open('day25.txt').read().splitlines())
        for j, val in enumerate(line):
            grid[j + 1, i + 1] = val
    step = 1
    while True:
        move = False
        # Move right
        new_grid = {}
        for (x, y) in grid:
            if grid[(x, y)] == '>':
                if x < width and grid[(x + 1, y)] == '.':
                    new_grid[(x, y)] = '.'
                    new_grid[(x + 1, y)] = '>'
                    move = True
                elif x == width and grid[(1, y)] == '.':
                    new_grid[(x, y)] = '.'
                    new_grid[(1, y)] = '>'
                    move = True
                elif (x, y) not in new_grid:
                    new_grid[(x, y)] = grid[(x, y)]
            elif (x, y) not in new_grid:
                new_grid[(x, y)] = grid[(x, y)]
        grid = new_grid
        new_grid = {}
        for (x, y) in grid:
            if grid[(x, y)] == 'v':
                if y < length and grid[(x, y + 1)] == '.':
                    new_grid[(x, y)] = '.'
                    new_grid[(x, y + 1)] = 'v'
                    move = True
                elif y == length and grid[(x, 1)] == '.':
                    new_grid[(x, y)] = '.'
                    new_grid[(x, 1)] = 'v'
                    move = True
                elif (x, y) not in new_grid:
                    new_grid[(x, y)] = grid[(x, y)]
            elif (x, y) not in new_grid:
                new_grid[(x, y)] = grid[(x, y)]
        grid = new_grid
        if not move:
            return step
        step += 1


if __name__ == '__main__':
    start_puzzle1 = int(round(time.time() * 1000))
    res_puzzle1 = puzzle1()
    end_puzzle1 = int(round(time.time() * 1000))
    print("Puzzle 1: " + str(res_puzzle1) + ". Took: " + str((end_puzzle1 - start_puzzle1)))
