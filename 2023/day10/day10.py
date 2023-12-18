import time
import os
from collections import defaultdict


os.chdir(os.path.dirname(os.path.abspath(__file__)))

def check_left(grid, curr):
    return grid[(curr[0], curr[1]-1)] == "-" or grid[(curr[0], curr[1]-1)] == "F" or grid[(curr[0], curr[1]-1)] == "L" or grid[(curr[0], curr[1]-1)] == "S"

def check_right(grid, curr):
    return grid[(curr[0], curr[1]+1)] == "-" or grid[(curr[0], curr[1]+1)] == "J" or grid[(curr[0], curr[1]+1)] == "7" or grid[(curr[0], curr[1]+1)] == "S"

def check_down(grid, curr):
    return grid[(curr[0]+1, curr[1])] == "|" or  grid[(curr[0]+1, curr[1])] == "J" or  grid[(curr[0]+1, curr[1])] == "L" or  grid[(curr[0]+1, curr[1])] == "S"

def check_up(grid, curr):
    return grid[(curr[0]-1, curr[1])] == "|" or grid[(curr[0]-1, curr[1])] == "7" or grid[(curr[0]-1, curr[1])] == "F" or grid[(curr[0]-1, curr[1])] == "S"

def get_neighbours(grid, curr):
    neighbours= []
    if grid[curr] in ["S", "|", "J", "L"] and check_up(grid, curr):
        neighbours.append((curr[0]-1, curr[1]))
    if grid[curr] in ["S","|", "F", "7"] and check_down(grid, curr):
        neighbours.append( (curr[0]+1, curr[1]))
    if grid[curr] in ["S","-", "J", "7"] and check_left(grid, curr):
        neighbours.append( (curr[0], curr[1]-1))
    if grid[curr] in ["S","-", "F", "L"] and check_right(grid, curr):
         neighbours.append( (curr[0], curr[1]+1))
    return neighbours

   

def puzzle1():
    grid = defaultdict(str)
    start = None
    for i, line in enumerate(open("day10.txt").readlines()):
        for j, val in enumerate(line.strip()):
            if val == "S":
                start = (i, j)
            if val != ".":
                grid[(i,j)] = val
    seen = {start}
    curr = get_neighbours(grid, start)
    distance = 0
    while True:
        distance += 1
        seen.update(curr)
        curr = [variable_name for location in curr for variable_name in get_neighbours(grid, location) if variable_name not in seen]
        if curr[0] == curr[1]:
            return distance + 1
        
        
                        

def puzzle2():
    grid = defaultdict(str)
    start = None
    for i, line in enumerate(open("day10.txt").readlines()):
        for j, val in enumerate(line.strip()):
            if val == "S":
                start = (i, j)
            if val != ".":
                grid[(i,j)] = val
    seen = {start}
    curr = get_neighbours(grid, start)
    while True:
        seen.update(curr)
        curr = [variable_name for location in curr for variable_name in get_neighbours(grid, location) if variable_name not in seen]
        if curr[0] == curr[1]:
            seen.update(curr)
            break
    res = 0
    for i, line in enumerate(open("day10.txt").readlines()):
        thomas_variable = 0
        last_symbol = ""
        max_j = max(j_2 if i_2 == i else 0 for (i_2, j_2) in seen)
        for j, val in enumerate(line.strip()):
            if j == max_j:
                break
            if (i, j) in seen and grid[(i,j)] == "|":
                thomas_variable += 1
            if (i, j) in seen and (grid[(i,j)] == "L" or grid[(i,j)] == "F"):  
                last_symbol = grid[(i,j)]
            if (i, j) in seen and grid[(i,j)] == "7" and last_symbol == "L":
                thomas_variable += 1
            if (i, j) in seen and grid[(i,j)] == "J" and last_symbol == "F":
                thomas_variable += 1
            if (i, j) not in seen and thomas_variable > 0 and thomas_variable % 2 == 1:
                print(i, j, thomas_variable)
                res += 1
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
