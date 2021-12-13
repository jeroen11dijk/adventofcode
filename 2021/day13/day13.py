import time


def puzzle1():
    points = set()
    folds = []
    for line in open('day13.txt').read().split("\n"):
        if line.__contains__(','):
            points.add((int(line.split(",")[0]), int(line.split(",")[1])))
        elif line.__contains__("fold"):
            folds.append(line.split()[-1])
    axis, value = folds[0].split("=")
    value = int(value)
    res = set()
    for point in points:
        if axis == "x":
            if point[0] > value:
                res.add((2 * value - point[0], point[1]))
            else:
                res.add(point)
        if axis == "y":
            if point[1] > value:
                res.add((point[0], 2 * value - point[1]))
            else:
                res.add(point)
    return len(res)


def puzzle2():
    points = set()
    folds = []
    for line in open('day13.txt').read().split("\n"):
        if line.__contains__(','):
            points.add((int(line.split(",")[0]), int(line.split(",")[1])))
        elif line.__contains__("fold"):
            folds.append(line.split()[-1])
    for fold in folds:
        axis, value = fold.split("=")
        value = int(value)
        res = set()
        for point in points:
            if axis == "x":
                if point[0] > value:
                    res.add((2 * value - point[0], point[1]))
                else:
                    res.add(point)
            if axis == "y":
                if point[1] > value:
                    res.add((point[0], 2 * value - point[1]))
                else:
                    res.add(point)
        points = res
    width = max(points, key=lambda x: x[0])[0] + 1
    height = max(points, key=lambda y: y[1])[1] + 1
    grid = [[' '] * width for _ in range(height)]
    for point in points:
        grid[point[1]][point[0]] = "#"
    for row in grid:
        print(row)
    return len(res)


if __name__ == '__main__':
    start_puzzle1 = int(round(time.time() * 1000))
    res_puzzle1 = puzzle1()
    end_puzzle1 = int(round(time.time() * 1000))
    print("Puzzle 1: " + str(res_puzzle1) + ". Took: " + str((end_puzzle1 - start_puzzle1)))
    start_puzzle2 = int(round(time.time() * 1000))
    res_puzzle2 = puzzle2()
    end_puzzle2 = int(round(time.time() * 1000))
    print("Puzzle 2: " + str(res_puzzle2) + ". Took: " + str((end_puzzle2 - start_puzzle2)))
