import time

directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]


def applyRule1(seatplan, row_len, column_len):
    new_seatplan = []
    is_changed = False
    for row in range(row_len):
        new_row = ""
        for column in range(column_len):
            if seatplan[row][column] == 'L':
                free_seats_around = 0
                for nbr in directions:
                    if 0 <= row + nbr[0] < row_len and 0 <= column + nbr[1] < column_len:
                        if seatplan[row + nbr[0]][column + nbr[1]] == '#':
                            free_seats_around += 1
                            new_row += 'L'
                            break
                if free_seats_around == 0:
                    is_changed = True
                    new_row += '#'
            elif seatplan[row][column] == '#':
                new_row += "#"
            else:
                new_row += '.'
        new_seatplan.append(new_row)
    return is_changed, new_seatplan


def applyRule2(seatplan, row_len, column_len):
    new_seatplan = []
    is_changed = False
    for row in range(row_len):
        new_row = ""
        for column in range(column_len):
            if seatplan[row][column] == '#':
                seats_around = 0
                for nbr in directions:
                    if 0 <= row + nbr[0] < row_len and 0 <= column + nbr[1] < column_len:
                        if seatplan[row + nbr[0]][column + nbr[1]] == '#':
                            if seatplan[row + nbr[0]][column + nbr[1]] == '#':
                                seats_around += 1
                if seats_around >= 4:
                    is_changed = True
                    new_row += 'L'
                else:
                    new_row += '#'
            elif seatplan[row][column] == 'L':
                new_row += "L"
            else:
                new_row += '.'
        new_seatplan.append(new_row)
    return is_changed, new_seatplan


def puzzle1():
    seatplan = [number.replace('L', '#') for number in open('day11.txt').read().split("\n")]
    row_len = len(seatplan)
    column_len = len(seatplan[0])
    is_changed, seatplan = applyRule2(seatplan, row_len, column_len)
    apply_rule = 1
    while is_changed:
        if apply_rule:
            is_changed, seatplan = applyRule1(seatplan, row_len, column_len)
            apply_rule = 0
        else:
            is_changed, seatplan = applyRule2(seatplan, row_len, column_len)
            apply_rule = 1
    res = 0
    for row in range(len(seatplan)):
        for column in range(len(seatplan[0])):
            if seatplan[row][column] == '#':
                res += 1
    return res


def applyRule1Puzzle2(seatplan, row_len, column_len):
    new_seatplan = []
    is_changed = False
    for row in range(row_len):
        new_row = ""
        for column in range(column_len):
            if seatplan[row][column] == 'L':
                free_seats_around = 0
                for nbr in directions:
                    if 0 <= row + nbr[0] < row_len and 0 <= column + nbr[1] < column_len:
                        sees_row = row + nbr[0]
                        sees_column = column + nbr[1]
                        sees = seatplan[sees_row][sees_column]
                        while sees == '.' and 0 <= sees_row + nbr[0] < row_len \
                                and 0 <= sees_column + nbr[1] < column_len:
                            sees_row += nbr[0]
                            sees_column += nbr[1]
                            sees = seatplan[sees_row][sees_column]
                        if sees == '#':
                            free_seats_around += 1
                            new_row += 'L'
                            break
                if free_seats_around == 0:
                    is_changed = True
                    new_row += '#'
            elif seatplan[row][column] == '#':
                new_row += "#"
            else:
                new_row += '.'
        new_seatplan.append(new_row)
    return is_changed, new_seatplan


def applyRule2Puzzle2(seatplan, row_len, column_len):
    new_seatplan = []
    is_changed = False
    for row in range(row_len):
        new_row = ""
        for column in range(column_len):
            if seatplan[row][column] == '#':
                seats_around = 0
                for nbr in directions:
                    if 0 <= row + nbr[0] < row_len and 0 <= column + nbr[1] < column_len:
                        sees_row = row + nbr[0]
                        sees_column = column + nbr[1]
                        sees = seatplan[sees_row][sees_column]
                        while sees == '.' and 0 <= sees_row + nbr[0] < row_len \
                                and 0 <= sees_column + nbr[1] < column_len:
                            sees_row += nbr[0]
                            sees_column += nbr[1]
                            sees = seatplan[sees_row][sees_column]
                        if sees == '#':
                            seats_around += 1
                if seats_around >= 5:
                    is_changed = True
                    new_row += 'L'
                else:
                    new_row += '#'
            elif seatplan[row][column] == 'L':
                new_row += "L"
            else:
                new_row += '.'
        new_seatplan.append(new_row)
    return is_changed, new_seatplan


def puzzle2():
    seatplan = [number.replace('L', '#') for number in open('day11.txt').read().split("\n")]
    row_len = len(seatplan)
    column_len = len(seatplan[0])
    is_changed, seatplan = applyRule2Puzzle2(seatplan, row_len, column_len)
    apply_rule = 1
    while is_changed:
        if apply_rule:
            is_changed, seatplan = applyRule1Puzzle2(seatplan, row_len, column_len)
            apply_rule = 0
        else:
            is_changed, seatplan = applyRule2Puzzle2(seatplan, row_len, column_len)
            apply_rule = 1
    res = 0
    for row in range(len(seatplan)):
        for column in range(len(seatplan[0])):
            if seatplan[row][column] == '#':
                res += 1
    return res


if __name__ == '__main__':
    start_puzzle1 = int(round(time.time() * 1000))
    res_puzzle1 = puzzle1()
    end_puzzle1 = int(round(time.time() * 1000))
    print("Puzzle 1: " + str(res_puzzle1) + ". Took: " + str((end_puzzle1 - start_puzzle1)))
    start_puzzle2 = int(round(time.time() * 1000))
    res_puzzle2 = puzzle2()
    end_puzzle2 = int(round(time.time() * 1000))
    print("Puzzle 2: " + str(res_puzzle2) + ". Took: " + str((end_puzzle2 - start_puzzle2)))
