import time


def puzzle1():
    return sum([len(set([letter for letter in line.replace('\n', '')])) for line in open('day6.txt').read().split("\n\n")])


def puzzle2():
    return sum([sum([all([question in line for line in line.split('\n')]) for question in line.split('\n')[0]]) for line in open('day6.txt').read().split("\n\n")])


if __name__ == '__main__':
    start_puzzle1 = int(round(time.time() * 1000))
    res_puzzle1 = puzzle1()
    end_puzzle1 = int(round(time.time() * 1000))
    print("Puzzle 1 : " + str(res_puzzle1) + ". Took: " + str((end_puzzle1 - start_puzzle1)))
    start_puzzle2 = int(round(time.time() * 1000))
    res_puzzle2 = puzzle2()
    end_puzzle2 = int(round(time.time() * 1000))
    print("Puzzle 1 : " + str(res_puzzle2) + ". Took: " + str((end_puzzle2 - start_puzzle2)))
