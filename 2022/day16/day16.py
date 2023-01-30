import re
import time
from collections import deque, defaultdict
from dataclasses import dataclass, field
from queue import PriorityQueue


def dijkstra(graph, start):
    distances = {v: float('inf') for v in graph.keys()}
    visited = set()
    Q = PriorityQueue()
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
    return distances


@dataclass
class queue_entry:
    node: str = "AA"
    total_pressure: int = 0
    time: int = 1
    open_valves: set = field(default_factory=set)

    def __str__(self):
        return str([self.node, self.total_pressure, self.time, self.open_valves])

    def __repr__(self):
        return str([self.node, self.total_pressure, self.time, self.open_valves])


@dataclass
class queue_entry2:
    node: tuple = ("AA", "AA")
    total_pressure: int = 0
    time: tuple = (1, 1)
    open_valves: set = field(default_factory=set)

    def __str__(self):
        return str([self.node, self.total_pressure, self.time, self.open_valves])

    def __repr__(self):
        return str([self.node, self.total_pressure, self.time, self.open_valves])

    def __hash__(self):
        return hash((self.node, self.total_pressure, self.time))


def read_input():
    graph = {}
    flows = {}
    distances = {}
    for line in open('day16.txt').read().splitlines():
        node = re.findall('\w*[A-Z]\w*[A-Z]\w*', line)[0]
        graph[node] = re.findall('\w*[A-Z]\w*[A-Z]\w*', line)[1:]
        flows[node] = int(re.findall('[0-9]+', line)[0])
    for node in graph:
        distances[node] = dijkstra(graph, node)
    return graph, flows, distances


def puzzle1():
    res = 0
    graph, flows, distances = read_input()
    best = defaultdict(lambda: 0)
    q = deque()
    q.append(queue_entry())
    while len(q) > 0:
        current: queue_entry = q.popleft()
        if current.total_pressure > res:
            res = current.total_pressure
        for node in graph:
            if node not in current.open_valves and flows[node] > 0:
                pressure_gain = (30 - current.time - distances[current.node][node]) * flows[node]
                new_set = set(current.open_valves)
                new_set.add(node)
                new_time = current.time + distances[current.node][node] + 1
                if new_time <= 30 and current.total_pressure + pressure_gain > best[tuple(new_set)]:
                    best[tuple(new_set)] = current.total_pressure + pressure_gain
                    new_entry = queue_entry(node, current.total_pressure + pressure_gain, new_time, new_set)
                    q.append(new_entry)
    return res


def puzzle2():
    res = 0
    graph, flows, distances = read_input()
    q = deque()
    q.append(queue_entry2())
    seen = set()
    best = defaultdict(lambda: 0)
    while len(q) > 0:
        current: queue_entry2 = q.popleft()
        if current.total_pressure > res:
            res = current.total_pressure
        for node in graph:
            if node not in current.open_valves and flows[node] > 0:
                pressure_gain = (26 - current.time[0] - distances[current.node[0]][node]) * flows[node]
                pressure_gain2 = (26 - current.time[1] - distances[current.node[1]][node]) * flows[node]
                new_set = set(current.open_valves)
                new_set.add(node)
                if current.time[0] + distances[current.node[0]][
                    node] + 1 <= 26 and current.total_pressure + pressure_gain > best[tuple(new_set)]:
                    best[tuple(new_set)] = current.total_pressure + pressure_gain
                    new_time = (current.time[0] + distances[current.node[0]][node] + 1, current.time[1])
                    reverse_time = (current.time[1], current.time[0] + distances[current.node[0]][node] + 1)
                    new_entry = queue_entry2((node, current.node[1]), current.total_pressure + pressure_gain, new_time,
                                             new_set)
                    reverse_entry = queue_entry2((current.node[1], node), current.total_pressure + pressure_gain,
                                                 reverse_time, new_set)
                    if new_entry not in seen and reverse_entry not in seen:
                        q.append(new_entry)
                        seen.add(new_entry)
                if current.time[1] + distances[current.node[1]][
                    node] + 1 <= 26 and current.total_pressure + pressure_gain2 > best[tuple(new_set)]:
                    best[tuple(new_set)] = current.total_pressure + pressure_gain
                    new_time = (current.time[0], current.time[1] + distances[current.node[1]][node] + 1)
                    reverse_time = (current.time[1] + distances[current.node[1]][node] + 1, current.time[0])
                    new_entry = queue_entry2((current.node[0], node), current.total_pressure + pressure_gain2, new_time,
                                             new_set)
                    reverse_entry = queue_entry2((node, current.node[0]), current.total_pressure + pressure_gain2,
                                                 reverse_time, new_set)
                    if new_entry not in seen and reverse_entry not in seen:
                        q.append(new_entry)
                        seen.add(new_entry)
    return res


if __name__ == '__main__':
    start_puzzle1 = int(round(time.time() * 1000))
    res_puzzle1 = puzzle1()
    end_puzzle1 = int(round(time.time() * 1000))
    print("Puzzle 1: " + str(res_puzzle1) + ". Took: " + str((end_puzzle1 - start_puzzle1)))
    start_puzzle2 = int(round(time.time() * 1000))
    res_puzzle2 = puzzle2()
    end_puzzle2 = int(round(time.time() * 1000))
    print("Puzzle 2: " + str(res_puzzle2) + ". Took: " + str((end_puzzle2 - start_puzzle2)))
