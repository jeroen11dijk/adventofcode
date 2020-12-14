import time
from copy import copy


def puzzle1():
    mask = ""
    memory = {}
    for line in open('day14.txt'):
        command, value = line.split('=')
        command = command.strip()
        value = value.strip()
        if command == "mask":
            mask = value
        else:
            value = bin(int(value))[2:].zfill(36)
            memoryaddress = command[4:-1]
            masked_value = ""
            for i, bit in enumerate(value):
                if mask[i] != 'X':
                    masked_value += mask[i]
                else:
                    masked_value += bit
            memory[memoryaddress] = int(masked_value, 2)
    return sum(memory.values())


def puzzle2():
    mask = ""
    memory = {}
    for line in open('day14.txt'):
        command, value = line.split('=')
        command = command.strip()
        if command == "mask":
            mask = value.strip()
        else:
            memoryaddress = bin(int(command[4:-1]))[2:].zfill(36)
            masked_memoryaddress = ""
            for i, bit in enumerate(memoryaddress):
                if mask[i] == 'X':
                    masked_memoryaddress += "X"
                elif mask[i] == "1":
                    masked_memoryaddress += "1"
                else:
                    masked_memoryaddress += bit
            floating_memories = [masked_memoryaddress]
            for i, bit in enumerate(masked_memoryaddress):
                new_memories = []
                if bit == "X":
                    for floating_memory in floating_memories:
                        new_memories.append(floating_memory[:i] + "0" + floating_memory[i+1:])
                        new_memories.append(floating_memory[:i] + "1" + floating_memory[i+1:])
                    floating_memories = new_memories
            for floating_memory_address in floating_memories:
                memory[int(floating_memory_address, 2)] = int(value.strip())
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
