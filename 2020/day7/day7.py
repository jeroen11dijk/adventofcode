import time


dictionary = {}
for line in open('day7.txt'):
    key = line.split(' ')[0] + " " + line.split(' ')[1]
    value = {}
    if line.split(' ')[4] == "no":
        dictionary[key] = {}
    else:
        for i in range(4, len(line.split(' ')), 4):
            value[line.split(' ')[i + 1] + " " + line.split(' ')[i + 2]] = line.split(' ')[i]
        dictionary[key] = value


def tree_search(key):
    return any(new_key == "shiny gold" or tree_search(new_key) for new_key in dictionary[key].keys())


def shiny_bag_search(key):
    if not dictionary[key]:
        return 1
    return sum([int(v) * shiny_bag_search(k) for k, v in dictionary[key].items()]) + 1


def puzzle1():
    return sum(map(tree_search, dictionary.keys()))


def puzzle2():
    return shiny_bag_search("shiny gold") - 1


if __name__ == '__main__':
    start_puzzle1 = int(round(time.time() * 1000))
    res_puzzle1 = puzzle1()
    end_puzzle1 = int(round(time.time() * 1000))
    print("Puzzle 1: " + str(res_puzzle1) + ". Took: " + str((end_puzzle1 - start_puzzle1)))
    start_puzzle2 = int(round(time.time() * 1000))
    res_puzzle2 = puzzle2()
    end_puzzle2 = int(round(time.time() * 1000))
    print("Puzzle 2: " + str(res_puzzle2) + ". Took: " + str((end_puzzle2 - start_puzzle2)))
