import time


def puzzle1():
    visited = {(0, 0)}
    current = [0, 0]
    for move in open('day3.txt').read():
        if move == '>':
            current[0] += 1
            if tuple(current) not in visited:
                visited.add(tuple(current))
        if move == '<':
            current[0] -= 1
            if tuple(current) not in visited:
                visited.add(tuple(current))
        if move == '^':
            current[1] += 1
            if tuple(current) not in visited:
                visited.add(tuple(current))
        if move == 'v':
            current[1] -= 1
            if tuple(current) not in visited:
                visited.add(tuple(current))
    return len(visited)


def puzzle2():
    visited = {(0, 0): 2}
    current = [[0, 0], [0, 0]]
    for i, move in enumerate(open('day3.txt').read()):
        index = i % 2
        if move == '>':
            current[index][0] += 1
            if tuple(current[index]) not in visited:
                visited[tuple(current[index])] = 1
            else:
                visited[tuple(current[index])] += 1
        if move == '<':
            current[index][0] -= 1
            if tuple(current[index]) not in visited:
                visited[tuple(current[index])] = 1
            else:
                visited[tuple(current[index])] += 1
        if move == '^':
            current[index][1] += 1
            if tuple(current[index]) not in visited:
                visited[tuple(current[index])] = 1
            else:
                visited[tuple(current[index])] += 1
        if move == 'v':
            current[index][1] -= 1
            if tuple(current[index]) not in visited:
                visited[tuple(current[index])] = 1
            else:
                visited[tuple(current[index])] += 1
    return len(visited)


if __name__ == '__main__':
    start_puzzle1 = int(round(time.time() * 1000))
    res_puzzle1 = puzzle1()
    end_puzzle1 = int(round(time.time() * 1000))
    print("Puzzle 1: " + str(res_puzzle1) + ". Took: " + str((end_puzzle1 - start_puzzle1)))
    start_puzzle2 = int(round(time.time() * 1000))
    res_puzzle2 = puzzle2()
    end_puzzle2 = int(round(time.time() * 1000))
    print("Puzzle 2: " + str(res_puzzle2) + ". Took: " + str((end_puzzle2 - start_puzzle2)))
