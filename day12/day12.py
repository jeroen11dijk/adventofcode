import time
import math

directions = {0: "N", 1: "E", 2: "S", 3: "W"}


def puzzle1():
    lines = open('day12.txt').read().split("\n")
    current_direction = 1
    x_value, y_value = 0, 0
    for line in lines:
        command = line[0]
        value = int(line[1:])
        if command == "F":
            command = directions[current_direction]
        if command == "N":
            y_value += value
        elif command == "E":
            x_value += value
        elif command == "S":
            y_value -= value
        elif command == "W":
            x_value -= value
        if command == "R":
            current_direction = (current_direction + (value / 90)) % 4
        elif command == "L":
            current_direction = (current_direction - (value / 90)) % 4
    return abs(x_value) + abs(y_value)


def puzzle2():
    lines = open('day12.txt').read().split("\n")
    ship_x, ship_y, waypoint_x, waypoint_y = 0, 0, 10, 1
    for line in lines:
        command = line[0]
        value = int(line[1:])
        if command == "F":
            ship_x += value * waypoint_x
            ship_y += value * waypoint_y
        if command == "N":
            waypoint_y += value
        elif command == "E":
            waypoint_x += value
        elif command == "S":
            waypoint_y -= value
        elif command == "W":
            waypoint_x -= value
        if command == "R":
            value = -math.radians(value)
            new_waypoint_x = math.cos(value) * waypoint_x - math.sin(value) * waypoint_y
            new_waypoint_y = math.sin(value) * waypoint_x + math.cos(value) * waypoint_y
            waypoint_x, waypoint_y = round(new_waypoint_x), round(new_waypoint_y)
        elif command == "L":
            value = math.radians(value)
            new_waypoint_x = math.cos(value) * waypoint_x - math.sin(value) * waypoint_y
            new_waypoint_y = math.sin(value) * waypoint_x + math.cos(value) * waypoint_y
            waypoint_x, waypoint_y = round(new_waypoint_x), round(new_waypoint_y)
    return abs(ship_x) + abs(ship_y)


if __name__ == '__main__':
    start_puzzle1 = int(round(time.time() * 1000))
    res_puzzle1 = puzzle1()
    end_puzzle1 = int(round(time.time() * 1000))
    print("Puzzle 1: " + str(res_puzzle1) + ". Took: " + str((end_puzzle1 - start_puzzle1)))
    start_puzzle2 = int(round(time.time() * 1000))
    res_puzzle2 = puzzle2()
    end_puzzle2 = int(round(time.time() * 1000))
    print("Puzzle 2: " + str(res_puzzle2) + ". Took: " + str((end_puzzle2 - start_puzzle2)))
