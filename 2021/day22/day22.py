import time


def puzzle1():
    on = set()
    for line in open("day22.txt").readlines():
        instruction, ranges = line.split()
        x_range, y_range, z_range = ranges.split(",")
        x_min, x_max = [int(x) for x in x_range.replace("x=", "").split("..")]
        y_min, y_max = [int(y) for y in y_range.replace("y=", "").split("..")]
        z_min, z_max = [int(z) for z in z_range.replace("z=", "").split("..")]
        x_min, y_min, z_min = max(x_min, -50), max(y_min, -50), max(z_min, -50)
        x_max, y_max, z_max = min(x_max, 50), min(y_max, 50), min(z_max, 50)
        for x in range(x_min, x_max + 1):
            for y in range(y_min, y_max + 1):
                for z in range(z_min, z_max + 1):
                    if instruction == "on":
                        on.add((x, y, z))
                    elif instruction == "off":
                        on.discard((x, y, z))
    return len(on)


class Cube:
    def __init__(self, xrange, yrange, zrange):
        self.xrange = xrange
        self.yrange = yrange
        self.zrange = zrange
        self.on = True

    def volume(self):
        return (self.xrange[1] - self.xrange[0] + 1) * (self.yrange[1] - self.yrange[0] + 1) * (
                    self.zrange[1] - self.zrange[0] + 1)

    def overlap(self, other: 'Cube'):
        cond1 = self.xrange[1] < other.xrange[0]
        cond2 = self.xrange[0] > other.xrange[1]
        cond3 = self.yrange[1] < other.yrange[0]
        cond4 = self.yrange[0] > other.yrange[1]
        cond5 = self.zrange[1] < other.zrange[0]
        cond6 = self.zrange[0] > other.zrange[1]
        if cond1 or cond2 or cond3 or cond4 or cond5 or cond6:
            return None
        else:
            overlap_xrange = (max(self.xrange[0], other.xrange[0]), min(self.xrange[1], other.xrange[1]))
            overlap_yrange = (max(self.yrange[0], other.yrange[0]), min(self.yrange[1], other.yrange[1]))
            overlap_zrange = (max(self.zrange[0], other.zrange[0]), min(self.zrange[1], other.zrange[1]))
            return Cube(overlap_xrange, overlap_yrange, overlap_zrange)

    def __str__(self):
        return str(self.xrange) + str(self.yrange) + str(self.zrange)

    def __repr__(self):
        return str(self.xrange) + str(self.yrange) + str(self.zrange)


def puzzle2():
    cubes = []
    for line in open("day22.txt").readlines():
        instruction, ranges = line.split()
        x_range, y_range, z_range = ranges.split(",")
        xmin, xmax = [int(x) for x in x_range.replace("x=", "").split("..")]
        ymin, ymax = [int(y) for y in y_range.replace("y=", "").split("..")]
        zmin, zmax = [int(z) for z in z_range.replace("z=", "").split("..")]
        current = Cube((xmin, xmax), (ymin, ymax), (zmin, zmax))
        current.on = bool(instruction == "on")
        cubes.append(current)
    processed = []
    for cube in cubes:
        new_cubes = []
        for other in processed:
            new_cube = cube.overlap(other)
            if new_cube is not None:
                if other.on == cube.on:
                    new_cube.on = not cube.on
                else:
                    if other.on:
                        new_cube.on = False
                    else:
                        new_cube.on = True
                new_cubes.append(new_cube)
        if cube.on:
            processed.append(cube)
        processed.extend(new_cubes)
    res = 0
    for cube in processed:
        if cube.on:
            res += cube.volume()
        else:
            res -= cube.volume()
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
