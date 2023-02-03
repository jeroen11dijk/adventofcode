import time


def puzzle1():
    coords = {}
    for line in open('day5.txt'):
        start_x, start_y = line.split()[0].split(",")
        start_x, start_y = int(start_x), int(start_y)
        end_x, end_y = line.split()[-1].split(",")
        end_x, end_y = int(end_x), int(end_y)
        if start_x == end_x:
            for i in range(min(start_y, end_y), max(start_y, end_y) + 1):
                if (start_x, i) in coords:
                    coords[(start_x, i)] = coords[(start_x, i)] + 1
                else:
                    coords[(start_x, i)] = 1
        if start_y == end_y:
            for i in range(min(start_x, end_x), max(start_x, end_x) + 1):
                if (i, start_y) in coords:
                    coords[(i, start_y)] = coords[(i, start_y)] + 1
                else:
                    coords[(i, start_y)] = 1
    return sum([1 if coords[key] > 1 else 0 for key in coords])


def puzzle2():
    coords = {}
    for line in open('day5.txt'):
        start_x, start_y = line.split()[0].split(",")
        start_x, start_y = int(start_x), int(start_y)
        end_x, end_y = line.split()[-1].split(",")
        end_x, end_y = int(end_x), int(end_y)
        if start_x == end_x:
            for i in range(min(start_y, end_y), max(start_y, end_y) + 1):
                if (start_x, i) in coords:
                    coords[(start_x, i)] = coords[(start_x, i)] + 1
                else:
                    coords[(start_x, i)] = 1
        else:
            slope = int((start_y - end_y) / (start_x - end_x))
            offset = int(start_y - slope * start_x)
            for i in range(min(start_x, end_x), max(start_x, end_x) + 1):
                point = (i, int(slope * i + offset))
                if point in coords:
                    coords[point] = coords[point] + 1
                else:
                    coords[point] = 1
    return sum([1 if coords[key] > 1 else 0 for key in coords])


if __name__ == '__main__':
    start_puzzle1 = int(round(time.time() * 1000))
    res_puzzle1 = puzzle1()
    end_puzzle1 = int(round(time.time() * 1000))
    print("Puzzle 1: " + str(res_puzzle1) + ". Took: " + str((end_puzzle1 - start_puzzle1)))
    start_puzzle2 = int(round(time.time() * 1000))
    res_puzzle2 = puzzle2()
    end_puzzle2 = int(round(time.time() * 1000))
    print("Puzzle 2: " + str(res_puzzle2) + ". Took: " + str((end_puzzle2 - start_puzzle2)))
