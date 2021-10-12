import time
import hashlib

def puzzle1():
    key = "bgvyzdsv"
    number = 0
    while True:
        result = hashlib.md5(str(key+str(number)).encode('utf-8')).hexdigest()
        if result.startswith("00000"):
            return number
        number += 1


def puzzle2():
    key = "bgvyzdsv"
    number = 0
    while True:
        result = hashlib.md5(str(key + str(number)).encode('utf-8')).hexdigest()
        if result.startswith("000000"):
            return number
        number += 1


if __name__ == '__main__':
    start_puzzle1 = int(round(time.time() * 1000))
    res_puzzle1 = puzzle1()
    end_puzzle1 = int(round(time.time() * 1000))
    print("Puzzle 1: " + str(res_puzzle1) + ". Took: " + str((end_puzzle1 - start_puzzle1)))
    start_puzzle2 = int(round(time.time() * 1000))
    res_puzzle2 = puzzle2()
    end_puzzle2 = int(round(time.time() * 1000))
    print("Puzzle 2: " + str(res_puzzle2) + ". Took: " + str((end_puzzle2 - start_puzzle2)))
