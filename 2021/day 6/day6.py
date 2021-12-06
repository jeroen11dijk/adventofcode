import time


def puzzle1():
    data = [int(i) for i in open('day6.txt').read().split("\n\n")[0].split(",")]
    fishies = {}
    for i in range(9):
        fishies[i] = data.count(i)
    for _ in range(80):
        new_fishies = {0: fishies[1], 1: fishies[2], 2: fishies[3], 3: fishies[4], 4: fishies[5], 5: fishies[6],
                       6: fishies[0] + fishies[7], 7: fishies[8], 8: fishies[0]}
        fishies = new_fishies
    return sum(fishies.values())


def puzzle2():
    data = [int(i) for i in open('day6.txt').read().split("\n\n")[0].split(",")]
    fishies = {}
    for i in range(9):
        fishies[i] = data.count(i)
    for _ in range(100000):
        new_fishies = {0: fishies[1], 1: fishies[2], 2: fishies[3], 3: fishies[4], 4: fishies[5], 5: fishies[6],
                       6: fishies[0] + fishies[7], 7: fishies[8], 8: fishies[0]}
        fishies = new_fishies
    return sum(fishies.values())


if __name__ == '__main__':
    start_puzzle1 = int(round(time.time() * 1000))
    res_puzzle1 = puzzle1()
    end_puzzle1 = int(round(time.time() * 1000))
    print("Puzzle 1: " + str(res_puzzle1) + ". Took: " + str((end_puzzle1 - start_puzzle1)))
    start_puzzle2 = int(round(time.time() * 1000))
    res_puzzle2 = puzzle2()
    end_puzzle2 = int(round(time.time() * 1000))
    print("Puzzle 2: " + str(res_puzzle2) + ". Took: " + str((end_puzzle2 - start_puzzle2)))
