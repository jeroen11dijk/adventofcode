import time
from collections import defaultdict
import os
from heapq import heappush, heappop

os.chdir(os.path.dirname(os.path.abspath(__file__)))


class Node:
    def __init__(self, coordinates, last_direction, steps, distance, previous):
        self.coordinates = coordinates
        self.last_direction = last_direction
        self.steps = steps
        self.distance = distance
        self.previous = previous

    def __str__(self):
        return str(
            [
                self.coordinates,
                self.last_direction,
                self.steps,
                self.distance,
                self.previous,
            ]
        )

    def __repr__(self):
        return str(
            [
                self.coordinates,
                self.last_direction,
                self.steps,
                self.distance,
                self.previous,
            ]
        )
        
    def __hash__(self) -> int:
        return hash((self.coordinates[0], self.coordinates[1], self.last_direction[0], self.last_direction[1], self.steps))

    def __lt__(self, other):
        return (self.distance < other.distance)
    
def puzzle1():
    graph = {}
    costs = {}
    for i, row in enumerate(open("day17.txt").read().splitlines()):
        for j, val in enumerate(row):
            costs[(i, j)] = int(val)
    target = (
        len(open("day17.txt").read().splitlines()) - 1,
        len(open("day17.txt").read().splitlines()[0]) - 1,
    )
    for key in costs.keys():
        nbrs = []
        for i in [-1, 1]:
            updown = (key[0] + i, key[1])
            leftright = (key[0], key[1] + i)
            if updown in costs:
                nbrs.append(updown)
            if leftright in costs:
                nbrs.append(leftright)
        graph[key] = nbrs
    optimal_distances = defaultdict(lambda: float("inf"))
    max_distance = 9 * (target[0] + target[1])
    optimal_distances[target] = max_distance
    start = Node((0, 0), (0, 0), 0, 0, [])
    queue = [start]
    seen = {}
    while queue:
        current = heappop(queue)
        if hash(current) in seen and current.distance >= seen[hash(current)]:
            continue
        seen[hash(current)] = current.distance
        heuristic = abs(target[0] - current.coordinates[0]) + abs(
            target[1] - current.coordinates[1]
        )
        max_distance_to_location = 9 * (current.coordinates[0] + current.coordinates[1])
        if (
            current.coordinates == target
            or current.distance + heuristic > optimal_distances[target]
            or current.distance > max_distance_to_location
        ):
            continue
        for nbr_coords in graph[current.coordinates]:
            nbr_direction = (
                nbr_coords[0] - current.coordinates[0],
                nbr_coords[1] - current.coordinates[1],
            )
            if nbr_direction == current.last_direction and current.steps == 3:
                continue
            if nbr_direction == current.last_direction:
                nbr_steps = current.steps + 1
            else:
                nbr_steps = 1
            nbr_distance = current.distance + costs[nbr_coords]
            nbr_previous = [location for location in current.previous] + [
                current.coordinates
            ]
            nbr_node = Node(
                nbr_coords, nbr_direction, nbr_steps, nbr_distance, nbr_previous
            )
            if nbr_coords in current.previous:
                continue
            heappush(queue, nbr_node)
            if nbr_distance < optimal_distances[nbr_coords]:
                optimal_distances[nbr_coords] = nbr_distance
    return optimal_distances[target]


def puzzle2():
    graph = {}
    costs = {}
    for i, row in enumerate(open("day17.txt").read().splitlines()):
        for j, val in enumerate(row):
            costs[(i, j)] = int(val)
    target = (
        len(open("day17.txt").read().splitlines()) - 1,
        len(open("day17.txt").read().splitlines()[0]) - 1,
    )
    for key in costs.keys():
        nbrs = []
        for i in [-1, 1]:
            updown = (key[0] + i, key[1])
            leftright = (key[0], key[1] + i)
            if updown in costs:
                nbrs.append(updown)
            if leftright in costs:
                nbrs.append(leftright)
        graph[key] = nbrs
    optimal_distances = defaultdict(lambda: float("inf"))
    max_distance = 9 * (target[0] + target[1])
    optimal_distances[target] = max_distance
    start_down = Node((0, 0), (1, 0), 0, 0, [])
    start_right = Node((0, 0), (0, 1), 0, 0, [])
    queue = [start_down, start_right]
    seen = {}
    while queue:
        current = heappop(queue)
        if hash(current) in seen and current.distance >= seen[hash(current)]:
            continue
        seen[hash(current)] = current.distance
        heuristic = abs(target[0] - current.coordinates[0]) + abs(
            target[1] - current.coordinates[1]
        )
        max_distance_to_location = 9 * (current.coordinates[0] + current.coordinates[1])
        if (
            current.coordinates == target
            or current.distance + heuristic > optimal_distances[target]
            or current.distance > max_distance_to_location
        ):
            continue
        for nbr_coords in graph[current.coordinates]:
            nbr_direction = (
                nbr_coords[0] - current.coordinates[0],
                nbr_coords[1] - current.coordinates[1],
            )
            if nbr_direction == current.last_direction and current.steps == 10:
                continue
            if nbr_direction != current.last_direction and current.steps < 4:
                continue
            if nbr_direction == current.last_direction:
                nbr_steps = current.steps + 1
            else:
                nbr_steps = 1
            nbr_distance = current.distance + costs[nbr_coords]
            nbr_previous = [location for location in current.previous] + [
                current.coordinates
            ]
            nbr_node = Node(
                nbr_coords, nbr_direction, nbr_steps, nbr_distance, nbr_previous
            )
            if nbr_coords in current.previous:
                continue
            heappush(queue, nbr_node)
            if nbr_coords == target and nbr_steps >= 4:
                    optimal_distances[nbr_coords] = nbr_distance
            if nbr_distance < optimal_distances[nbr_coords] and nbr_coords != target:
                optimal_distances[nbr_coords] = nbr_distance
    return optimal_distances[target]


if __name__ == "__main__":
    start_puzzle1 = int(round(time.time() * 1000))
    res_puzzle1 = puzzle1()
    end_puzzle1 = int(round(time.time() * 1000))
    print(
        "Puzzle 1: "
        + str(res_puzzle1)
        + ". Took: "
        + str((end_puzzle1 - start_puzzle1))
    )
    start_puzzle2 = int(round(time.time() * 1000))
    res_puzzle2 = puzzle2()
    end_puzzle2 = int(round(time.time() * 1000))
    print(
        "Puzzle 2: "
        + str(res_puzzle2)
        + ". Took: "
        + str((end_puzzle2 - start_puzzle2))
    )
