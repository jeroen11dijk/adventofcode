import time


def puzzle1():
    players = open("day22.txt").read().split('\n\n')
    player1 = list(map(int, players[0].split("\n")[1:]))
    player2 = list(map(int, players[1].split("\n")[1:]))
    while len(player1) > 0 and len(player2) > 0:
        card1, card2 = player1.pop(0), player2.pop(0)
        if card1 > card2:
            player1.append(card1)
            player1.append(card2)
        else:
            player2.append(card2)
            player2.append(card1)
    if len(player1) > 0:
        return sum([(i + 1) * val for i, val in enumerate(reversed(player1))])
    if len(player2) > 0:
        return sum([(i + 1) * val for i, val in enumerate(reversed(player2))])


def play_game(player1, player2):
    seen = set()
    while len(player1) > 0 and len(player2) > 0:
        card_state = (tuple(player1), tuple(player2))
        if card_state in seen:
            return True, sum([(i + 1) * val for i, val in enumerate(reversed(player1))])
        seen.add(card_state)
        card1, card2 = player1.pop(0), player2.pop(0)
        if card1 <= len(player1) and card2 <= len(player2):
            winner, _ = play_game(player1[:card1], player2[:card2])
            if winner:
                player1.append(card1)
                player1.append(card2)
            else:
                player2.append(card2)
                player2.append(card1)
        elif card1 > card2:
            player1.append(card1)
            player1.append(card2)
        else:
            player2.append(card2)
            player2.append(card1)
    if len(player1) > 0:
        return True, sum([(i + 1) * val for i, val in enumerate(reversed(player1))])
    if len(player2) > 0:
        return False, sum([(i + 1) * val for i, val in enumerate(reversed(player2))])


def puzzle2():
    players = open("day22.txt").read().split('\n\n')
    player1 = list(map(int, players[0].split("\n")[1:]))
    player2 = list(map(int, players[1].split("\n")[1:]))
    return play_game(player1, player2)[1]


if __name__ == '__main__':
    start_puzzle1 = int(round(time.time() * 1000))
    res_puzzle1 = puzzle1()
    end_puzzle1 = int(round(time.time() * 1000))
    print("Puzzle 1: " + str(res_puzzle1) + ". Took: " + str((end_puzzle1 - start_puzzle1)))
    start_puzzle2 = int(round(time.time() * 1000))
    res_puzzle2 = puzzle2()
    end_puzzle2 = int(round(time.time() * 1000))
    print("Puzzle 2: " + str(res_puzzle2) + ". Took: " + str((end_puzzle2 - start_puzzle2)))
