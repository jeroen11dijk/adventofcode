import time
from collections import defaultdict


class Puzzle():
    def __init__(self):
        self.line = open('day17.txt').read()
        self.windindex = 0
        self.grid = defaultdict(lambda: ".")
        for x in range(8):
            self.grid[x, 0] = "-"
        self.floor = 0

    def place_rock(self, index, floor):
        if index % 5 == 0:
            return [(i, floor + 4) for i in range(3, 7)]
        if index % 5 == 1:
            return [(4, floor + 4), (3, floor + 5), (4, floor + 5), (5, floor + 5), (4, floor + 6)]
        if index % 5 == 2:
            return [(3, floor + 4), (4, floor + 4), (5, floor + 4), (5, floor + 5), (5, floor + 6)]
        if index % 5 == 3:
            return [(3, floor + 4 + i) for i in range(4)]
        if index % 5 == 4:
            return [(3, floor + 4), (3, floor + 5), (4, floor + 4), (4, floor + 5)]

    def do_movement(self, current):
        while True:
            move = False
            wind = self.line[self.windindex]
            self.windindex = (self.windindex + 1) % len(self.line)
            if wind == ">":
                if all(self.grid[(point[0] + 1, point[1])] == "." and point[0] + 1 < 8 for point in current):
                    current = [(x[0] + 1, x[1]) for x in current]
            elif wind == "<":
                if all(self.grid[(point[0] - 1, point[1])] == "." and point[0] - 1 > 0 for point in current):
                    current = [(x[0] - 1, x[1]) for x in current]
            if all(self.grid[(point[0], point[1] - 1)] == "." for point in current):
                current = [(x[0], x[1] - 1) for x in current]
                move = True
            if not move:
                for point in current:
                    self.floor = max(self.floor, point[1])
                    self.grid[point] = "@"
                break

    def solve1(self):
        for rock in range(2022):
            current = self.place_rock(rock, self.floor)
            self.do_movement(current)
        return self.floor

    def solve2(self):
        states = {}
        inarow = 0
        rock = 0
        total_rocks = 1000000000000
        floordifference, rockdifference = None, None
        while rock <= total_rocks:
            # Place rock
            current = self.place_rock(rock, self.floor)
            if (rock % 5, self.windindex) not in states:
                inarow = 0
                states[(rock % 5, self.windindex)] = (self.floor, rock)
            else:
                inarow += 1
            if inarow == 5:
                floordifference = self.floor - states[(rock % 5, self.windindex)][0]
                rockdifference = rock - states[(rock % 5, self.windindex)][1]

            if floordifference and rockdifference and (total_rocks - rock) % rockdifference == 0:
                amount_of_repetitions = (total_rocks - rock) // rockdifference
                rock += amount_of_repetitions * rockdifference
                self.floor += amount_of_repetitions * floordifference
            # do movement
            self.do_movement(current)
            rock += 1
        return self.floor


if __name__ == '__main__':
    start_puzzle1 = int(round(time.time() * 1000))
    res_puzzle1 = Puzzle().solve1()
    end_puzzle1 = int(round(time.time() * 1000))
    print("Puzzle 1: " + str(res_puzzle1) + ". Took: " + str((end_puzzle1 - start_puzzle1)))
    start_puzzle2 = int(round(time.time() * 1000))
    res_puzzle2 = Puzzle().solve2()
    end_puzzle2 = int(round(time.time() * 1000))
    print("Puzzle 2: " + str(res_puzzle2) + ". Took: " + str((end_puzzle2 - start_puzzle2)))
