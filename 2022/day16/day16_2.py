import heapq
import re
import time
from copy import deepcopy
from dataclasses import dataclass, field
from queue import PriorityQueue

class FastContainsPriorityQueue:
    def __init__(self):
        self.pq = []
        self.cs = {}

    def __contains__(self, item) -> bool:
        return item in self.cs

    def enqueue(self, item):
        heapq.heappush(self.pq, item)
        if item in self.cs:
            self.cs[item] += 1
        else:
            self.cs[item] = 1

    def dequeue(self):
        item = heapq.heappop(self.pq)

        if item in self.cs:
            if self.cs[item] > 1:
                self.cs[item] -= 1
            else:
                del self.cs[item]

        return item

    def empty(self) -> bool:
        return len(self.pq) == 0

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
    total_pressure: int = 0
    pressure_gain: int = 0
    time: int = 1
    node: str = "AA"
    open_valves: set = field(default_factory=set)

    def __lt__(self, other):
        return -self.pressure_gain < -other.pressure_gain

    def __str__(self):
        return str([self.total_pressure, self.pressure_gain, self.time, self.node, self.open_valves])

    def __repr__(self):
        return str([self.total_pressure, self.pressure_gain, self.time, self.node, self.open_valves])

    def __hash__(self):
        return hash((self.total_pressure, self.pressure_gain, self.time, self.node))


def calculate_heuristic(current, timestep, open_valves, flows, distances):
    res = 0
    order = sorted([x for x in flows if x not in open_valves], key=lambda x: flows[x], reverse=True)
    for node in order:
        if timestep + distances[current][node] + 1 <= 30:
            res += (30 - timestep - distances[current][node]) * flows[node]
            timestep += distances[current][node] + 1
    return res*2


def puzzle1():
    res = 0
    graph = {}
    flows = {}
    distances = {}
    for line in open('day16.txt').read().splitlines():
        node = re.findall('\w*[A-Z]\w*[A-Z]\w*', line)[0]
        graph[node] = re.findall('\w*[A-Z]\w*[A-Z]\w*', line)[1:]
        if int(re.findall('[0-9]+', line)[0]) > 0:
            flows[node] = int(re.findall('[0-9]+', line)[0])
    for node in graph:
        distances[node] = dijkstra(graph, node)
    Q = FastContainsPriorityQueue()
    Q.enqueue(queue_entry())
    while not Q.empty():
        current: queue_entry = Q.dequeue()
        if current.time == 30:
            res = max(res, current.total_pressure)
        else:
            # We can open the current valve in which case we increase pressure_gain
            new_time = current.time + 1
            if current.node not in current.open_valves and current.node in flows:
                new_set = deepcopy(current.open_valves)
                new_set.add(current.node)
                new_gain = current.pressure_gain + flows[current.node]
                new_pressure = current.total_pressure + new_gain
                heuristic = calculate_heuristic(current.node, new_time, new_set, flows, distances)
                if new_pressure + heuristic > res:
                    new_entry = queue_entry(new_pressure, new_gain, new_time, current.node, new_set)
                    Q.enqueue(new_entry)
            # Or we move to a neighboring node
            for nbr in graph[current.node]:
                new_pressure = current.total_pressure + current.pressure_gain
                heuristic = calculate_heuristic(current.node, new_time, current.open_valves, flows, distances)
                if new_pressure + heuristic > res:
                    new_entry = queue_entry(new_pressure, current.pressure_gain, new_time, nbr,
                                            current.open_valves)
                    Q.enqueue(new_entry)
    return res


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
