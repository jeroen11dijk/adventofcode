import time
from copy import copy


def puzzle1():
    mask = ""
    memory = {}
    for line in open('day14.txt'):
        command, value = line.split(' = ')
        if command == "mask":
            mask = value
        else:
            masked_value = ""
            for i, bit in enumerate(bin(int(value))[2:].zfill(36)):
                if mask[i] != 'X':
                    masked_value += mask[i]
                else:
                    masked_value += bit
            memory[command[4:-1]] = int(masked_value, 2)
    return sum(memory.values())


def puzzle2():
    mask = ""
    memory = {}
    for line in open('day14.txt'):
        command, value = line.split(' = ')
        if command == "mask":
            mask = value.strip()
        else:
            memoryaddress = bin(int(command[4:-1]))[2:].zfill(36)
            masked_memoryaddress = ""
            for i, bit in enumerate(memoryaddress):
                if mask[i] == 'X' or mask[i] == "1":
                    masked_memoryaddress += mask[i]
                else:
                    masked_memoryaddress += bit
            memories = [masked_memoryaddress]
            for i, bit in enumerate(masked_memoryaddress):
                new_memories = []
                if bit == "X":
                    for floating_memory in memories:
                        new_memories.append(floating_memory[:i] + "0" + floating_memory[i + 1:])
                        new_memories.append(floating_memory[:i] + "1" + floating_memory[i + 1:])
                    memories = new_memories
            for floating_memory_address in memories:
                memory[int(floating_memory_address, 2)] = int(value)
    return sum(memory.values())


if __name__ == '__main__':
    start_puzzle1 = int(round(time.time() * 1000))
    res_puzzle1 = puzzle1()
    end_puzzle1 = int(round(time.time() * 1000))
    print("Puzzle 1: " + str(res_puzzle1) + ". Took: " + str((end_puzzle1 - start_puzzle1)))
    start_puzzle2 = int(round(time.time() * 1000))
    res_puzzle2 = puzzle2()
    end_puzzle2 = int(round(time.time() * 1000))
    print("Puzzle 2: " + str(res_puzzle2) + ". Took: " + str((end_puzzle2 - start_puzzle2)))
