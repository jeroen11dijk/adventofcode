import re
import time
from collections import deque


def puzzle1():
    cubes = []
    cubesset = set()
    res = 0
    for line in open('day18.txt').read().splitlines():
        cube = [int(x) for x in re.findall("\d+", line)]
        cubes.append(cube)
        cubesset.add(tuple(cube))
    for cube in cubes:
        res += 6
        for dir in [[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]]:
            res -= int((cube[0] + dir[0], cube[1] + dir[1], cube[2] + dir[2]) in cubesset)
    return res


def bfs(node, lava, minx, maxx, miny, maxy, minz, maxz):
    visited = set()
    Q = deque()
    Q.append(node)
    good = False
    while len(Q) > 0:
        current = Q.pop()
        visited.add(current)
        for dir in [[-1, 0, 0], [1, 0, 0], [0, -1, 0], [0, 1, 0], [0, 0, -1], [0, 0, 1]]:
            nbr = (current[0] + dir[0], current[1] + dir[1], current[2] + dir[2])
            if nbr not in visited:
                if nbr not in lava and minx <= nbr[0] <= maxx and miny <= nbr[1] <= maxy and minz <= nbr[2] <= maxz:
                    Q.append(nbr)
                elif nbr not in lava:
                    good = True
    return good, visited


def puzzle2():
    cubes = []
    lava = set()
    air = set()
    res = 0
    minx, maxx, miny, maxy, minz, maxz = float("inf"), -1, float("inf"), -1, float("inf"), -1
    for line in open('day18.txt').read().splitlines():
        cube = [int(x) for x in re.findall("\d+", line)]
        minx, maxx = min(minx, cube[0] - 1), max(maxx, cube[0] + 1)
        miny, maxy = min(miny, cube[1] - 1), max(maxy, cube[1] + 1)
        minz, maxz = min(minz, cube[2] - 1), max(maxz, cube[2] + 1)
        cubes.append(cube)
        lava.add(tuple(cube))
    for cube in cubes:
        for dir in [[-1, 0, 0], [1, 0, 0], [0, -1, 0], [0, 1, 0], [0, 0, -1], [0, 0, 1]]:
            nbr = (cube[0] + dir[0], cube[1] + dir[1], cube[2] + dir[2])
            if nbr in air:
                res += 1
            elif nbr not in lava:
                good, visited = bfs(nbr, lava, minx, maxx, miny, maxy, minz, maxz)
                if good:
                    res += 1
                    air.update(visited)
                else:
                    lava.update(visited)
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
