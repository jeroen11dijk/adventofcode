import time


def puzzle1():
    with open('day1.txt') as f:
        data = f.readlines()[0]
        return data.count('(') - data.count(')')


def puzzle2():
    floor = 0
    with open('day1.txt') as f:
        for i, move in enumerate(f.readlines()[0]):
            if move == '(':
                floor += 1
            elif move == ')':
                floor -= 1
            if floor == -1:
                return i+1

if __name__ == '__main__':
    start_puzzle1 = int(round(time.time() * 1000))
    res_puzzle1 = puzzle1()
    end_puzzle1 = int(round(time.time() * 1000))
    print("Puzzle 1: " + str(res_puzzle1) + ". Took: " + str((end_puzzle1 - start_puzzle1)))
    start_puzzle2 = int(round(time.time() * 1000))
    res_puzzle2 = puzzle2()
    end_puzzle2 = int(round(time.time() * 1000))
    print("Puzzle 2: " + str(res_puzzle2) + ". Took: " + str((end_puzzle2 - start_puzzle2)))
