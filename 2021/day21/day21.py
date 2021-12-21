import time


def puzzle1():
    one = int(open("day21.txt").read().split('\n')[0].split()[-1])
    two = int(open("day21.txt").read().split('\n')[1].split()[-1])
    die = 1
    one_score, two_score = 0, 0
    while one_score < 1000 and two_score < 1000:
        for _ in range(3):
            one = (one + die - 1) % 10 + 1
            die += 1
        one_score += one
        if one_score >= 1000:
            break
        for _ in range(3):
            two = (two + die - 1) % 10 + 1
            die += 1
        two_score += two
    return min(one_score, two_score) * (die - 1)


DIRAC = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}


def throw_die(one, two, p1):
    one_wins, two_wins = 0, 0
    for roll, weight in DIRAC.items():
        if p1:
            new_one = ((one[0] + roll - 1) % 10 + 1, one[1] + ((one[0] + roll - 1) % 10 + 1))
            new_two = two
        else:
            new_one = one
            new_two = ((two[0] + roll - 1) % 10 + 1, two[1] + ((two[0] + roll - 1) % 10 + 1))
        if new_one[1] >= 21 and p1:
            one_wins += weight
        elif new_two[1] >= 21 and not p1:
            two_wins += weight
        else:
            a, b = throw_die(new_one, new_two, not p1)
            one_wins += a * weight
            two_wins += b * weight

    return one_wins, two_wins


def puzzle2():
    one = (int(open("day21.txt").read().split('\n')[0].split()[-1]), 0)
    two = (int(open("day21.txt").read().split('\n')[1].split()[-1]), 0)
    return max(throw_die(one, two, True))


if __name__ == '__main__':
    start_puzzle1 = int(round(time.time() * 1000))
    res_puzzle1 = puzzle1()
    end_puzzle1 = int(round(time.time() * 1000))
    print("Puzzle 1: " + str(res_puzzle1) + ". Took: " + str((end_puzzle1 - start_puzzle1)))
    start_puzzle2 = int(round(time.time() * 1000))
    res_puzzle2 = puzzle2()
    end_puzzle2 = int(round(time.time() * 1000))
    print("Puzzle 2: " + str(res_puzzle2) + ". Took: " + str((end_puzzle2 - start_puzzle2)))
