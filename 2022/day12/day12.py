import time
from queue import PriorityQueue


def generate_graph(all_starts=False):
    grid = []
    graph = {}
    starts = []
    for i, line in enumerate(open('day12.txt').read().splitlines()):
        grid.append([val for val in line])
        for j, val in enumerate(line):
            if val == "S":
                start = (j, i)
                starts.append((j, i))
                grid[i][j] = 'a'
            if val == "E":
                goal = (j, i)
                grid[i][j] = 'z'
            if val == "a":
                starts.append((j, i))
    for i in range(len(grid[0])):
        for j in range(len(grid)):
            neighbours = []
            if i != 0 and ord(grid[j][i]) + 1 >= ord(grid[j][i - 1]):
                neighbours.append((i - 1, j))
            if i != len(grid[0]) - 1 and ord(grid[j][i]) + 1 >= ord(grid[j][i + 1]):
                neighbours.append((i + 1, j))
            if j != 0 and ord(grid[j][i]) + 1 >= ord(grid[j - 1][i]):
                neighbours.append((i, j - 1))
            if j != len(grid) - 1 and ord(grid[j][i]) + 1 >= ord(grid[j + 1][i]):
                neighbours.append((i, j + 1))
            graph[(i, j)] = neighbours
    if all_starts:
        return graph, starts, goal
    return graph, start, goal


def dijkstra(graph, starts, goal):
    distances = {v: float('inf') for v in graph.keys()}
    visited = set()
    Q = PriorityQueue()
    for start in starts:
        distances[start] = 0
        Q.put((0, start))
    while not Q.empty():
        dist, current = Q.get()
        visited.add(current)
        for nbr in graph[current]:
            if nbr not in visited:
                if distances[current] + 1 < distances[nbr]:
                    Q.put((distances[current] + 1, nbr))
                    distances[nbr] = distances[current] + 1
    return distances[goal]


def puzzle1():
    graph, start, goal = generate_graph()
    return dijkstra(graph, [start], goal)


def puzzle2():
    graph, starts, goal = generate_graph(True)
    return dijkstra(graph, starts, goal)


if __name__ == '__main__':
    start_puzzle1 = int(round(time.time() * 1000))
    res_puzzle1 = puzzle1()
    end_puzzle1 = int(round(time.time() * 1000))
    print("Puzzle 1: " + str(res_puzzle1) + ". Took: " + str((end_puzzle1 - start_puzzle1)))
    start_puzzle2 = int(round(time.time() * 1000))
    res_puzzle2 = puzzle2()
    end_puzzle2 = int(round(time.time() * 1000))
    print("Puzzle 2: " + str(res_puzzle2) + ". Took: " + str((end_puzzle2 - start_puzzle2)))
