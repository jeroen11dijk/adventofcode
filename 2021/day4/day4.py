import time


def puzzle1():
    bingo = [int(i) for i in open('day4.txt').read().split("\n")[0].split(",")]
    rows = []
    columns = []
    for i in range(int((len(open('day4.txt').read().split("\n")) - 1) / 6)):
        card = open('day4.txt').read().split("\n")[6 * i + 1:6 * i + 7]
        card.remove(card[0])
        row = []
        column = [set() for _ in range(len(card[0].split()))]
        for idk in card:
            row.append(set([int(value) for value in idk.split()]))
            for i, value in enumerate(idk.split()):
                column[i].add(int(value))
        rows.append(row)
        columns.append(column)
    for number in bingo:
        for i in range(len(rows)):
            for row in rows[i]:
                row.discard(number)
                if len(row) == 0:
                    return number * sum(sum(tmp) for tmp in rows[i])
            for column in columns[i]:
                column.discard(number)
                if len(column) == 0:
                    return number * sum(sum(tmp) for tmp in columns[i])


def puzzle2():
    bingo = [int(i) for i in open('day4.txt').read().split("\n")[0].split(",")]
    rows = []
    columns = []
    cards = set()
    for i in range(int((len(open('day4.txt').read().split("\n")) - 1) / 6)):
        cards.add(i)
        card = open('day4.txt').read().split("\n")[6 * i + 1:6 * i + 7]
        card.remove(card[0])
        row = []
        column = [set() for _ in range(len(card[0].split()))]
        for idk in card:
            row.append(set([int(value) for value in idk.split()]))
            for i, value in enumerate(idk.split()):
                column[i].add(int(value))
        rows.append(row)
        columns.append(column)
    for number in bingo:
        for i in range(len(rows)):
            for row in rows[i]:
                row.discard(number)
                if len(row) == 0:
                    cards.discard(i)
                    if len(cards) == 0:
                        return number * sum(sum(tmp) for tmp in rows[i])
            for column in columns[i]:
                column.discard(number)
                if len(column) == 0:
                    cards.discard(i)
                    if len(cards) == 0:
                        return number * sum(sum(tmp) for tmp in columns[i])



if __name__ == '__main__':
    start_puzzle1 = int(round(time.time() * 1000))
    res_puzzle1 = puzzle1()
    end_puzzle1 = int(round(time.time() * 1000))
    print("Puzzle 1: " + str(res_puzzle1) + ". Took: " + str((end_puzzle1 - start_puzzle1)))
    start_puzzle2 = int(round(time.time() * 1000))
    res_puzzle2 = puzzle2()
    end_puzzle2 = int(round(time.time() * 1000))
    print("Puzzle 2: " + str(res_puzzle2) + ". Took: " + str((end_puzzle2 - start_puzzle2)))
