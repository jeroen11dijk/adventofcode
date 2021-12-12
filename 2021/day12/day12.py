import time


class path:
    def __init__(self, location, visited, visited_twice, path):
        self.location = location
        self.visited = visited
        self.visit_twice = visited_twice
        self.path = path

    def __str__(self):
        return str(self.path)

    def __repr__(self):
        return str(self.path)


def create_graph():
    graph = {}
    for line in open('day12.txt').read().split("\n"):
        a, b = line.split("-")
        if a not in graph:
            graph[a] = [b]
        else:
            graph[a].append(b)
        if b not in graph:
            graph[b] = [a]
        else:
            graph[b].append(a)
    return graph


def puzzle1():
    graph = create_graph()
    res = 0
    queue = [path("start", {"start"}, False, [])]
    while queue:
        current = queue.pop()
        for nbr in graph[current.location]:
            if nbr == "end":
                res += 1
            elif nbr not in current.visited:
                next = path(nbr, set(current.visited), current.visit_twice, current.path + [nbr])
                if nbr.islower():
                    next.visited.add(nbr)
                queue.append(next)
    return res


def puzzle2():
    graph = create_graph()
    res = 0
    queue = [path("start", {"start"}, False, [])]
    while queue:
        current = queue.pop()
        for nbr in graph[current.location]:
            if nbr == "end":
                res += 1
            elif nbr not in current.visited:
                next = path(nbr, set(current.visited), current.visit_twice, current.path + [nbr])
                if nbr.islower():
                    next.visited.add(nbr)
                queue.append(next)
            elif nbr in current.visited and not current.visit_twice and nbr != "start":
                next = path(nbr, set(current.visited), True, current.path + [nbr])
                if nbr.islower():
                    next.visited.add(nbr)
                queue.append(next)
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
