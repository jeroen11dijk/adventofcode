import time

from lark.exceptions import LarkError
from lark.lark import Lark


def puzzle1():
    players = open("day22.txt").read().split('\n\n')
    player1 = players[0].split("\n")[1:]
    player2 = players[1].split("\n")[1:]
    while len(player1) > 0 and len(player2) > 0:
        card1 = int(player1.pop(0))
        card2 = int(player2.pop(0))
        if card1 > card2:
            player1.append(card1)
            player1.append(card2)
        else:
            player2.append(card2)
            player2.append(card1)
    if len(player1) > 0:
        return sum([(i + 1) * int(val) for i, val in enumerate(reversed(player1))])
    if len(player2) > 0:
        return sum([(i + 1) * int(val) for i, val in enumerate(reversed(player2))])


def puzzle2():
    return 0


if __name__ == '__main__':
    start_puzzle1 = int(round(time.time() * 1000))
    res_puzzle1 = puzzle1()
    end_puzzle1 = int(round(time.time() * 1000))
    print("Puzzle 1: " + str(res_puzzle1) + ". Took: " + str((end_puzzle1 - start_puzzle1)))
    start_puzzle2 = int(round(time.time() * 1000))
    res_puzzle2 = puzzle2()
    end_puzzle2 = int(round(time.time() * 1000))
    print("Puzzle 2: " + str(res_puzzle2) + ". Took: " + str((end_puzzle2 - start_puzzle2)))
