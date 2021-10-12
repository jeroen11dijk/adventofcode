import itertools
import time
from _collections import deque


def move(cups, current, max_score):
    index = cups.index(current)
    three = list(itertools.islice(cups, index + 1, index + 4))
    if len(three) < 3:
        three.extend(list(itertools.islice(cups, 0, 3 - len(three))))
    three = deque(three)
    for val in three:
        cups.remove(val)
    destination = current - 1
    while destination not in cups:
        destination -= 1
        if destination < 1:
            destination = max_score
    destination_index = cups.index(destination)
    for i, val in enumerate(three, 1):
        cups.insert(destination_index + i, val)
    return cups, cups[(cups.index(current) + 1) % len(cups)]


def puzzle1():
    cups = deque(map(int, open("day23.txt").read()))
    current = cups[0]
    for i in range(100):
        cups, current = move(cups, current, 9)
    index_one = cups.index(1)
    res = list(itertools.islice(cups, index_one + 1, len(cups)))
    res.extend(list(itertools.islice(cups, 0, index_one)))
    return "".join([str(val) for val in res])


class Cup:
    def __init__(self, label: int) -> None:
        self.label = label
        self.next = None

    def __repr__(self):
        return f"Cup number: {self.label}"


def puzzle2():
    labels = list(map(int, open("day23.txt").read()))
    number_cups = 1000000
    labels = [int(label) for label in labels]
    # Need a way of finding the place of a cup given its label - hence dict[int, Cup]
    # Create a million cups with no next cup
    lookup_table = {i: Cup(i) for i in range(1, number_cups + 1)}

    # Set each cup to have the numerically next cup as its successor
    for i in range(1, number_cups):
        lookup_table[i].next = lookup_table[i + 1]

    # Point the last cup in the list to the first in the specified order
    lookup_table[number_cups].next = lookup_table[labels[0]]

    # Arrange the first 9 cups according to the specified order
    for i in range(len(labels)):
        lookup_table[labels[i]].next = lookup_table[labels[(i + 1) % len(labels)]]

    # repoint the last cup in the specified list to the correct place (currently points back to the first cup)
    if number_cups > len(labels):
        lookup_table[labels[-1]].next = lookup_table[len(labels) + 1]

    # Start with the first cup in the specifed order
    current_cup = lookup_table[labels[0]]

    for _ in range(10000000):
        # Remove the selection of 3 from the linked list
        selection = current_cup.next
        current_cup.next = current_cup.next.next.next.next
        seek = current_cup.label - 1 if current_cup.label > 1 else number_cups
        while seek in [current_cup.label, selection.label, selection.next.label, selection.next.next.label]:
            seek -= 1
            if seek < 1:
                seek = number_cups

        next_cup = lookup_table[seek]
        selection.next.next.next = next_cup.next
        next_cup.next = selection
        current_cup = current_cup.next

    return lookup_table[1].next.label * lookup_table[1].next.next.label


if __name__ == '__main__':
    start_puzzle1 = int(round(time.time() * 1000))
    res_puzzle1 = puzzle1()
    end_puzzle1 = int(round(time.time() * 1000))
    print("Puzzle 1: " + str(res_puzzle1) + ". Took: " + str((end_puzzle1 - start_puzzle1)))
    start_puzzle2 = int(round(time.time() * 1000))
    res_puzzle2 = puzzle2()
    end_puzzle2 = int(round(time.time() * 1000))
    print("Puzzle 2: " + str(res_puzzle2) + ". Took: " + str((end_puzzle2 - start_puzzle2)))
