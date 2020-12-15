import time


def puzzle(target):
    starting_numbers = list(map(int, open('day15.txt').read().split(",")))
    occurences = {value: [i + 1] for i, value in enumerate(starting_numbers)}
    last_number = starting_numbers[-1]
    len_starting_numbers = len(starting_numbers)
    for i in range(len_starting_numbers + 1, target + 1):
        if last_number not in occurences or i == len(starting_numbers) + 1:
            last_number = 0
            if last_number in occurences:
                occurences[last_number].append(i)
            else:
                occurences[last_number] = [i]
        else:
            last_number_occurences = occurences[last_number]
            if len(last_number_occurences) == 1:
                last_number = i - 1 - occurences[last_number][0]
            else:
                last_number = last_number_occurences[-1] - last_number_occurences[-2]
            if last_number in occurences:
                occurences[last_number].append(i)
            else:
                occurences[last_number] = [i]
    return last_number


if __name__ == '__main__':
    start_puzzle1 = int(round(time.time() * 1000))
    res_puzzle1 = puzzle(2020)
    end_puzzle1 = int(round(time.time() * 1000))
    print("Puzzle 1: " + str(res_puzzle1) + ". Took: " + str((end_puzzle1 - start_puzzle1)))
    start_puzzle2 = int(round(time.time() * 1000))
    res_puzzle2 = puzzle(30000000)
    end_puzzle2 = int(round(time.time() * 1000))
    print("Puzzle 2: " + str(res_puzzle2) + ". Took: " + str((end_puzzle2 - start_puzzle2)))
