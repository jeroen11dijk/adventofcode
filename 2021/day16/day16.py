import time
from functools import reduce

hexToBinaryTable = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110',
                    '7': '0111', '8': '1000', '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101',
                    'E': '1110', 'F': '1111'}


def parse_packet(input):
    res = int(input[:3], 2)
    id = int(input[3:6], 2)
    if id == 4:
        index = 6
        while True:
            index += 5
            if int(input[index - 5]) == 0:
                break
        input = input[index:]
        return res, input
    else:
        if int(input[6]) == 0:
            length = int(input[7:22], 2)
            subpackets = input[22: 22 + length]
            while len(subpackets) > 0:
                version, subpackets = parse_packet(subpackets)
                res += version
            return res, input[22 + length:]
        elif int(input[6]) == 1:
            n_subpackets = int(input[7:18], 2)
            subpackets = input[18:]
            for _ in range(n_subpackets):
                version, subpackets = parse_packet(subpackets)
                res += version
            return res, subpackets
    return res, ""


def puzzle1():
    hex = open('day16.txt').read()
    binary = ""
    for i in hex:
        binary += hexToBinaryTable[i]
    res, _ = parse_packet(binary)
    return res


def convert_values(values, id):
    if id == 0:
        return sum(values)
    elif id == 1:
        return reduce(lambda x, y: x * y, values)
    elif id == 2:
        return min(values)
    elif id == 3:
        return max(values)
    elif id == 5:
        return 1 if values[0] > values[1] else 0
    elif id == 6:
        return 1 if values[0] < values[1] else 0
    elif id == 7:
        return 1 if values[0] == values[1] else 0


def get_value(input):
    id = int(input[3:6], 2)
    if id == 4:
        index = 6
        bit_string = ""
        while True:
            bit_string += input[index + 1:index + 5]
            index += 5
            if int(input[index - 5]) == 0:
                break
        input = input[index:]
        return int(bit_string, 2), input
    else:
        values = []
        if int(input[6]) == 0:
            length = int(input[7:22], 2)
            subpackets = input[22: 22 + length]
            while len(subpackets) > 0:
                value, subpackets = get_value(subpackets)
                values.append(value)
            return convert_values(values, id), input[22 + length:]
        elif int(input[6]) == 1:
            n_subpackets = int(input[7:18], 2)
            subpackets = input[18:]
            for _ in range(n_subpackets):
                value, subpackets = get_value(subpackets)
                values.append(value)
            return convert_values(values, id), subpackets
    return None, ""


def puzzle2():
    hex = open('day16.txt').read()
    binary = ""
    for i in hex:
        binary += hexToBinaryTable[i]
    res, _ = get_value(binary)
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
