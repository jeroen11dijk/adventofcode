import time


def puzzle1():
    adapters = sorted([int(number) for number in open('day10.txt').read().split("\n")] + [0])
    adapters.append(max(adapters) + 3)
    jolt1 = 0
    jolt3 = 0
    for i in range(1, len(adapters)):
        if adapters[i] - adapters[i - 1] == 1:
            jolt1 += 1
        if adapters[i] - adapters[i - 1] == 3:
            jolt3 += 1
    return jolt1 * jolt3


def puzzle2():
    adapters = sorted([int(number) for number in open('day10.txt').read().split("\n")] + [0])
    adapters.append(max(adapters) + 3)
    total = 1
    index = 0
    while True:
        possibilities = [x for x in adapters if adapters[index] < x <= adapters[index] + 3]
        if index >= len(adapters) - 1:
            break
        if len(possibilities) == 1:
            index += 1
        elif len(possibilities) == 2:
            next = adapters[index + 3]
            can_reach_next = 0
            for i in possibilities:
                if i + 3 >= next:
                    can_reach_next += 1
            if can_reach_next == 1:
                total *= 2
            elif can_reach_next == 2:
                total *= 3
            index += 3
        elif len(possibilities) == 3:
            next = adapters[index + 4]
            can_reach_next = 0
            for i in possibilities:
                if i + 3 >= next:
                    can_reach_next += 1
            if can_reach_next == 1:
                total *= 4
            elif can_reach_next == 2:
                total *= 6
            elif can_reach_next == 3:
                total *= 7
            index += 4
    return total


def puzzle2Dynamic():
    adapters = sorted([int(number) for number in open('day10.txt').read().split("\n")])
    adapters.append(max(adapters) + 3)
    results = [0] * (max(adapters) + 1)
    results[0] = 1
    for adapter in adapters:
        results[adapter] = results[adapter - 1] + results[adapter - 2] + results[adapter - 3]
    return results[-1]


if __name__ == '__main__':
    start_puzzle1 = int(round(time.time() * 1000))
    res_puzzle1 = puzzle1()
    end_puzzle1 = int(round(time.time() * 1000))
    print("Puzzle 1: " + str(res_puzzle1) + ". Took: " + str((end_puzzle1 - start_puzzle1)))
    start_puzzle2 = int(round(time.time() * 1000))
    res_puzzle2 = puzzle2()
    end_puzzle2 = int(round(time.time() * 1000))
    print("Puzzle 2: " + str(res_puzzle2) + ". Took: " + str((end_puzzle2 - start_puzzle2)))
