import time

from tqdm import tqdm

convert = {"=": -2, "-": -1, "0": 0, "1": 1, "2": 2}


def convert_SNAFU_int(line):
    total = 0
    for i, val in enumerate(reversed(line)):
        total += (5 ** i) * convert[val]
    return total


def puzzle1():
    total = sum([convert_SNAFU_int(line) for line in open('day25.txt').read().splitlines()])
    count = {0: "=", 1: "-", 2: "0", 3: "1", 4: "2"}
    start = [4,4,4,4,4,4,4,4,4,4,4,4,0,2,3,3,1,3,1,4]
    start_value = convert_SNAFU_int("".join(list(reversed([count[x] for x in start]))))
    print(start_value - total)
    for _ in tqdm(range(start_value, total)):
        start[0] += 1
        index = 0
        while start[index] > 4:
            start[index] = 0
            if len(start) - 1 == index:
                start.append(3)
            else:
                start[index + 1] += 1
                index += 1
        snafu = list(reversed([count[x] for x in start]))
    return "".join(snafu)


if __name__ == '__main__':
    start_puzzle1 = int(round(time.time() * 1000))
    res_puzzle1 = puzzle1()
    end_puzzle1 = int(round(time.time() * 1000))
    print("Puzzle 1: " + str(res_puzzle1) + ". Took: " + str((end_puzzle1 - start_puzzle1)))
