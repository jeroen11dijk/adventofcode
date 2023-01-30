import time


def check_left_right(left, right):
    for i, val in enumerate(left):
        if i == len(right):
            return False
        elif isinstance(val, int) and isinstance(right[i], int):
            if val < right[i]:
                return True
            if val > right[i]:
                return False
        elif isinstance(val, list) and isinstance(right[i], list):
            comp = check_left_right(val, right[i])
            if comp is not None:
                return comp
        elif isinstance(val, list) and isinstance(right[i], int):
            comp = check_left_right(val, [right[i]])
            if comp is not None:
                return comp
        elif isinstance(val, int) and isinstance(right[i], list):
            comp = check_left_right([val], right[i])
            if comp is not None:
                return comp
    if len(left) < len(right):
        return True
    if len(left) == len(right):
        return None
    if len(left) > len(right):
        return False


def puzzle1():
    res = 0
    for i, line in enumerate(open('day13.txt').read().split("\n\n")):
        left, right = [eval(x) for x in line.split("\n")]
        print(check_left_right(left, right))
        if check_left_right(left, right) is None or check_left_right(left, right) == 1:
            res += i + 1
    return res


def partition(data, low, high):
    pivot = data[high]
    i = low - 1
    for j in range(low, high):
        if check_left_right(data[j], pivot):
            i = i + 1
            data[i], data[j] = data[j], data[i]
    data[i + 1], data[high] = data[high], data[i + 1]
    return i + 1


def quicksort(data, low, high):
    if low < high:
        pivot = partition(data, low, high)
        quicksort(data, low, pivot - 1)
        quicksort(data, pivot + 1, high)


def puzzle2():
    items = [[2], [6]]
    for line in open('day13.txt').read().split("\n\n"):
        items.extend([eval(x) for x in line.split("\n")])
    quicksort(items, 0, len(items) - 1)
    return (items.index([2]) + 1) * (items.index([6]) + 1)


if __name__ == '__main__':
    start_puzzle1 = int(round(time.time() * 1000))
    res_puzzle1 = puzzle1()
    end_puzzle1 = int(round(time.time() * 1000))
    print("Puzzle 1: " + str(res_puzzle1) + ". Took: " + str((end_puzzle1 - start_puzzle1)))
    start_puzzle2 = int(round(time.time() * 1000))
    res_puzzle2 = puzzle2()
    end_puzzle2 = int(round(time.time() * 1000))
    print("Puzzle 2: " + str(res_puzzle2) + ". Took: " + str((end_puzzle2 - start_puzzle2)))
