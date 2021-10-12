import time
from functools import reduce


def puzzle1():
    res = float("inf")
    bus_id = 0
    depart, busses = open('day13.txt').read().split("\n")
    depart = int(depart)
    busses = busses.split(",")
    for bus in busses:
        if bus != "x":
            original_bus = int(bus)
            bus = int(bus)
            while bus < depart:
                bus += original_bus
            wait_time = bus - depart
            if wait_time < res:
                res = wait_time
                bus_id = original_bus
    return bus_id * res


def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1


def puzzle2():
    _, busses = open('day13.txt').read().split("\n")
    busses = busses.split(",")
    n = []
    a = []
    for i, bus in enumerate(busses):
        if bus != "x":
            n.append(int(bus))
            a.append((-i) % int(bus))
    return chinese_remainder(n, a)


if __name__ == '__main__':
    start_puzzle1 = int(round(time.time() * 1000))
    res_puzzle1 = puzzle1()
    end_puzzle1 = int(round(time.time() * 1000))
    print("Puzzle 1: " + str(res_puzzle1) + ". Took: " + str((end_puzzle1 - start_puzzle1)))
    start_puzzle2 = int(round(time.time() * 1000))
    res_puzzle2 = puzzle2()
    end_puzzle2 = int(round(time.time() * 1000))
    print("Puzzle 2: " + str(res_puzzle2) + ". Took: " + str((end_puzzle2 - start_puzzle2)))
