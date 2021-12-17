import time


def project_line(x, y, x_range, y_range):
    xmin, xmax = int(x_range[0]), int(x_range[1])
    ymin, ymax = int(y_range[0]), int(y_range[1])
    start = [0, 0]
    max_height = 0
    while start[0] <= xmax and start[1] >= ymin:
        start[0] += x
        start[1] += y
        if start[1] > max_height:
            max_height = start[1]
        if x < 0:
            x += 1
        elif x > 0:
            x -= 1
        y -= 1
        if xmin <= start[0] <= xmax and ymin <= start[1] <= ymax:
            return max_height
    return -1


def puzzle1():
    line = open('day17.txt').read()
    res = 0
    x = line.split()[-2].replace("x=", "").replace(",", "").split("..")
    y = line.split()[-1].replace("y=", "").replace(",", "").split("..")
    for i in range(-300, 300):
        for j in range(0, 500):
            height = project_line(i, j, x, y)
            res = max(res, height)
    return res


def puzzle2():
    line = open('day17.txt').read()
    res = 0
    x = line.split()[-2].replace("x=", "").replace(",", "").split("..")
    y = line.split()[-1].replace("y=", "").replace(",", "").split("..")
    for i in range(-300, 300):
        for j in range(-300, 300):
            height = project_line(i, j, x, y)
            if height > -1:
                res += 1
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
