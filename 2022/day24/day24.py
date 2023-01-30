import time
from collections import defaultdict, deque


class Puzzle:

    def __init__(self):
        grid = []
        for i, line in enumerate(open('day24.txt').read().splitlines()):
            grid.append([val for val in line])
        self.graph = {}
        self.obstacles = defaultdict(lambda: defaultdict(list))
        self.minx, self.maxx, self.miny, self.maxy = 1, len(grid[0]) - 2, 1, len(grid) - 2
        for y, row in enumerate(grid):
            for x, val in enumerate(row):
                if val != "#":
                    nbrs = [(x, y)]
                    if x + 1 <= self.maxx and grid[y][x + 1] != "#":
                        nbrs.append((x + 1, y))
                    if y - 1 >= self.miny and grid[y - 1][x] != "#":
                        nbrs.append((x, y - 1))
                    if x - 1 >= self.minx and grid[y][x - 1] != "#":
                        nbrs.append((x - 1, y))
                    if y + 1 <= self.maxy and grid[y + 1][x] != "#":
                        nbrs.append((x, y + 1))
                    if y == self.maxy and x == self.maxx:
                        nbrs.append((x, y + 1))
                    if y == self.miny and x == self.minx:
                        nbrs.append((x, y - 1))
                    self.graph[(x, y)] = nbrs
                if val != "." and val != "#":
                    self.obstacles[0][x, y].append(val)

    def generate_blizzard(self, index):
        for key in self.obstacles[index]:
            winds = self.obstacles[index][key]
            for direction in winds:
                if direction == ">":
                    if (key[0] + 1, key[1]) in self.graph[key]:
                        self.obstacles[index + 1][(key[0] + 1, key[1])].append(">")
                    else:
                        self.obstacles[index + 1][(self.minx, key[1])].append(">")
                if direction == "<":
                    if (key[0] - 1, key[1]) in self.graph[key]:
                        self.obstacles[index + 1][(key[0] - 1, key[1])].append("<")
                    else:
                        self.obstacles[index + 1][(self.maxx, key[1])].append("<")
                if direction == "^":
                    if (key[0], key[1] - 1) in self.graph[key]:
                        self.obstacles[index + 1][(key[0], key[1] - 1)].append("^")
                    else:
                        self.obstacles[index + 1][(key[0], self.maxy)].append("^")
                if direction == "v":
                    if (key[0], key[1] + 1) in self.graph[key]:
                        self.obstacles[index + 1][(key[0], key[1] + 1)].append("v")
                    else:
                        self.obstacles[index + 1][(key[0], self.miny)].append("v")

    def find_path(self, start_time, start, goal):
        index = start_time
        Q = deque()
        Q.append(start)
        while True:
            self.generate_blizzard(index)
            index += 1
            newQ = deque()
            seen = set()
            while len(Q) > 0:
                current = Q.pop()
                for nbr in self.graph[current]:
                    if nbr == goal:
                        return index
                    if nbr not in self.obstacles[index] and nbr not in seen:
                        newQ.append(nbr)
                        seen.add(nbr)
            Q = newQ


def puzzle1():
    puzzle = Puzzle()
    return puzzle.find_path(0, (1, 0), (puzzle.maxx, puzzle.maxy + 1))


def puzzle2():
    puzzle = Puzzle()
    go = puzzle.find_path(0, (1, 0), (puzzle.maxx, puzzle.maxy + 1))
    get_snacks = puzzle.find_path(go,(puzzle.maxx, puzzle.maxy + 1), (1, 0))
    return puzzle.find_path(get_snacks, (1, 0), (puzzle.maxx, puzzle.maxy + 1))


if __name__ == '__main__':
    start_puzzle1 = int(round(time.time() * 1000))
    res_puzzle1 = puzzle1()
    end_puzzle1 = int(round(time.time() * 1000))
    print("Puzzle 1: " + str(res_puzzle1) + ". Took: " + str((end_puzzle1 - start_puzzle1)))
    start_puzzle2 = int(round(time.time() * 1000))
    res_puzzle2 = puzzle2()
    end_puzzle2 = int(round(time.time() * 1000))
    print("Puzzle 2: " + str(res_puzzle2) + ". Took: " + str((end_puzzle2 - start_puzzle2)))
