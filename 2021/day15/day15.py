import time
from queue import PriorityQueue


def dijkstra(dist, values):
    visited = set()
    height = width = max(dist)[0] + 1
    src = (0, 0)
    dist[src] = 0
    queue = PriorityQueue()
    queue.put((0, src))
    visited.add(src)
    while not queue.empty():
        _, current = queue.get()
        visited.add(current)
        for direction in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nbr = (current[0] + direction[0], current[1] + direction[1])
            if -1 < nbr[0] < height and -1 < nbr[1] < width and nbr not in visited:
                new_dist = dist[current] + values[nbr]
                if new_dist < dist[nbr]:
                    dist[nbr] = new_dist
                    queue.put((new_dist, nbr))
    return dist


def puzzle1():
    values = {}
    dist = {}
    for i, line in enumerate(open('day15.txt').read().split("\n")):
        for j, value in enumerate(line):
            values[(i, j)] = int(value)
            dist[(i, j)] = float("inf")
    return dijkstra(dist, values)[max(dist)]


def enlarge_grid():
    grid = []
    for i, line in enumerate(open('day15.txt').read().split("\n")):
        grid.append([])
        for value in line:
            grid[i].append(int(value))
    for row in range(len(grid)):
        original = grid[row].copy()
        for i in range(1, 5):
            grid[row].extend([(x + i - 1) % 9 + 1 for x in original])
    final = grid.copy()
    for i in range(1, 5):
        for row in grid:
            final.append([(x + i - 1) % 9 + 1 for x in row])
    return final


def puzzle2():
    grid = enlarge_grid()
    values = {}
    dist = {}
    for i, line in enumerate(grid):
        for j, value in enumerate(line):
            values[(i, j)] = int(value)
            dist[(i, j)] = float("inf")
    return dijkstra(dist, values)[max(dist)]


if __name__ == '__main__':
    start_puzzle1 = int(round(time.time() * 1000))
    res_puzzle1 = puzzle1()
    end_puzzle1 = int(round(time.time() * 1000))
    print("Puzzle 1: " + str(res_puzzle1) + ". Took: " + str((end_puzzle1 - start_puzzle1)))
    start_puzzle2 = int(round(time.time() * 1000))
    res_puzzle2 = puzzle2()
    end_puzzle2 = int(round(time.time() * 1000))
    print("Puzzle 2: " + str(res_puzzle2) + ". Took: " + str((end_puzzle2 - start_puzzle2)))
