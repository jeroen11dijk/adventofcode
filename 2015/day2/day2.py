import time


def puzzle1():
    res = 0
    for gift in open('day2.txt').read().split("\n"):
        gift = gift.split('x')
        sides = [int(gift[0]) * int(gift[1]), int(gift[0])*int(gift[2]), int(gift[1])*int(gift[2])]
        res += 2*sum(sides) + min(sides)
    return res


def puzzle2():
    res = 0
    for gift in open('day2.txt').read().split("\n"):
        gift = gift.split('x')
        sides = [int(gift[0]), int(gift[1]), int(gift[2])]
        sides.sort()
        res += 2*sides[0] + 2*sides[1]
        res += sides[0]*sides[1]*sides[2]
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
