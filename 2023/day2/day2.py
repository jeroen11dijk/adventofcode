import time
import re


def check_games(games):
    min_red, min_green, min_blue = 0, 0, 0
    for game in games.split(";"):
        for color in game.split(","):
            number = int(re.findall(r"\d+", color)[0])
            if "red" in color and number > min_red:
                min_red = number
            if "green" in color and number > min_green:
                min_green = number
            if "blue" in color and number > min_blue:
                min_blue = number
    return min_red, min_green, min_blue


def puzzle1():
    res = 0
    for line in open("day2.txt").readlines():
        game_info, games = line.split(":")
        game_id = int(re.findall(r"\d+", game_info)[0])
        min_red, min_green, min_blue = check_games(games)
        if min_red <= 12 and min_green <= 13 and min_blue <= 14:
            res += game_id
    return res


def puzzle2():
    res = 0
    for line in open("day2.txt").readlines():
        _, games = line.split(":")
        min_red, min_green, min_blue = check_games(games)
        res += min_red * min_green * min_blue
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
