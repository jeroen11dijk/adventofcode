import time
import os
from collections import Counter
from dataclasses import dataclass

os.chdir(os.path.dirname(os.path.abspath(__file__)))


@dataclass
class Game:
    hand: str
    bid: int
    score: int

    def __lt__(self, other):
        if self.score < other.score:
            return True
        if self.score > other.score:
            return False
        for card_self, card_other in zip(self.hand, other.hand):
            if convert_plaatje(card_self) != convert_plaatje(card_other):
                return convert_plaatje(card_self) < convert_plaatje(card_other)


def convert_plaatje(char):
    if char == "T":
        return 10
    if char == "J":
        return -1
    if char == "Q":
        return 12
    if char == "K":
        return 13
    if char == "A":
        return 14
    return int(char)


def puzzle1():
    res = 0
    lines = open("day7.txt").read().splitlines()
    games = []
    for line in lines:
        hand, bid = line.split()
        counter_hand = Counter(hand).most_common()
        if counter_hand[0][1] == 5:
            games.append(Game(hand, bid, 7))
            continue
        if counter_hand[0][1] == 4:
            games.append(Game(hand, bid, 6))
            continue
        if counter_hand[0][1] == 3 and counter_hand[1][1] == 2:
            games.append(Game(hand, bid, 5))
            continue
        if counter_hand[0][1] == 3:
            games.append(Game(hand, bid, 4))
            continue
        if counter_hand[0][1] == 2 and counter_hand[1][1] == 2:
            games.append(Game(hand, bid, 3))
            continue
        if counter_hand[0][1] == 2:
            games.append(Game(hand, bid, 2))
            continue
        if counter_hand[0][1] == 1:
            games.append(Game(hand, bid, 1))
            continue
    games.sort()
    for i, game in enumerate(games):
        res += (i + 1) * int(game.bid)
    return res

def puzzle2():
    res = 0
    games = []
    for line in  open("day7.txt").read().splitlines():
        hand, bid = line.split()
        counter_hand = Counter(hand).most_common()
        start_index = 0
        if hand == "JJJJJ":
            most_common_value = "J"
        else:
            most_common_value = counter_hand[start_index][0]
            while most_common_value == "J":
                most_common_value = counter_hand[start_index][0]
                start_index += 1
        if Counter("".join( [char if char != "J" else most_common_value for char in hand])).most_common()[0][1] == 5:
            games.append(Game("".join( [char if char != "J" else "1" for char in hand]), bid, 7))
            continue
        if Counter("".join( [char if char != "J" else most_common_value for char in hand])).most_common()[0][1] == 4:
            games.append(Game("".join( [char if char != "J" else "1" for char in hand]), bid, 6))
            continue
        if Counter("".join( [char if char != "J" else most_common_value for char in hand])).most_common()[0][1] == 3 and counter_hand[1][1] == 2:
            games.append(Game("".join( [char if char != "J" else "1" for char in hand]), bid, 5))
            continue
        if Counter("".join( [char if char != "J" else most_common_value for char in hand])).most_common()[0][1] == 3:
            games.append(Game("".join( [char if char != "J" else "1" for char in hand]), bid, 4))
            continue
        if Counter("".join( [char if char != "J" else most_common_value for char in hand])).most_common()[0][1] == 2 and counter_hand[1][1] == 2:
            games.append(Game("".join( [char if char != "J" else "1" for char in hand]), bid, 3))
            continue
        if Counter("".join( [char if char != "J" else most_common_value for char in hand])).most_common()[0][1] == 2:
            games.append(Game("".join( [char if char != "J" else "1" for char in hand]), bid, 2))
            continue
        if Counter("".join( [char if char != "J" else most_common_value for char in hand])).most_common()[0][1] == 1:
            games.append(Game("".join( [char if char != "J" else "1" for char in hand]), bid, 1))
            continue
    games.sort()
    for game in games:
        print(game)
    for i, game in enumerate(games):
        res += (i + 1) * int(game.bid)
    return res

if __name__ == "__main__":
    start_puzzle1 = int(round(time.time() * 1000))
    res_puzzle1 = puzzle1()
    end_puzzle1 = int(round(time.time() * 1000))
    print(
        "Puzzle 1: "
        + str(res_puzzle1)
        + ". Took: "
        + str((end_puzzle1 - start_puzzle1))
    )
    start_puzzle2 = int(round(time.time() * 1000))
    res_puzzle2 = puzzle2()
    end_puzzle2 = int(round(time.time() * 1000))
    print(
        "Puzzle 2: "
        + str(res_puzzle2)
        + ". Took: "
        + str((end_puzzle2 - start_puzzle2))
    )
