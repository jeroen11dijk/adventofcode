import time
import os
from collections import defaultdict

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def puzzle1():
    res = 0
    for sequence in open("day15.txt").read().split(","):
        hash = 0
        for val in sequence:
            hash += ord(val)
            hash *= 17
            hash = hash % 256
        res += hash
    return res


def puzzle2():
    res = 0
    hashmap = defaultdict(list)
    for sequence in open("day15.txt").read().split(","):
        hash = 0
        for val in sequence:
            if val == "=":
                label = sequence.split("=")[0]
                focal_length = int(sequence.split("=")[1])
                replaced = False
                for i, elem in enumerate(hashmap[hash]):
                    if elem[0] == label:
                        hashmap[hash][i] = (label, focal_length)
                        replaced = True
                        break
                if not replaced:
                    hashmap[hash].append((label, focal_length))
                break
            if val == "-":
                label = sequence.split("-")[0]
                for i, elem in enumerate(hashmap[hash]):
                    if elem[0] == label:
                        hashmap[hash].remove(elem)
                        break
                break
            hash += ord(val)
            hash *= 17
            hash = hash % 256
    for key,val in sorted(hashmap.items()):
        for slot, focal in enumerate(val):
            res += (key + 1) * (slot + 1) * focal[1]
    return res

if __name__ == "__main__":
    start_puzzle1 = int(round(time.time() * 1000))
    res_puzzle1 = puzzle1()
    end_puzzle1 = int(round(time.time() * 1000))
    print(
        "Puzzle 1: "
        + str(res_puzzle1)
        + ". Took: "
        + str((end_puzzle1 - start_puzzle1))
    )
    start_puzzle2 = int(round(time.time() * 1000))
    res_puzzle2 = puzzle2()
    end_puzzle2 = int(round(time.time() * 1000))
    print(
        "Puzzle 2: "
        + str(res_puzzle2)
        + ". Took: "
        + str((end_puzzle2 - start_puzzle2))
    )
