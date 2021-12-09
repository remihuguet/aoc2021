from functools import reduce


def read_input(input_file):
    with open(input_file, "r") as f:
        return [i for i in f.readlines()]


def find_minima(input_file: str):
    data = [[int(i) for i in line.replace("\n", "")] for line in read_input(input_file)]

    minima = set()
    i_max, j_max = len(data), len(data[0])
    for i, line in enumerate(data):
        for j, value in enumerate(line):
            neighbors = []
            if i > 0:
                neighbors.append(data[i - 1][j])
            if i < i_max - 1:
                neighbors.append(data[i + 1][j])
            if j > 0:
                neighbors.append(data[i][j - 1])
            if j < j_max - 1:
                neighbors.append(data[i][j + 1])
            if all([value < v for v in neighbors]):
                minima.add((i, j, value))
    return minima, data, i_max, j_max


def compute_risk(input_file: str):
    minima, _, _, _ = find_minima(input_file)
    return sum([i[2] + 1 for i in minima])


def compute_size_of_basins(input_file: str):
    minima, data, i_max, j_max = find_minima(input_file)
    basins = []
    for m in minima:
        i, j, value = m
        basins.append(get_basin_neighbors(i, j, data, i_max, j_max, set([m])))
    return reduce(
        lambda t, e: t * e,
        [len(b) for b in list(sorted(basins, key=lambda b: len(b)))][-3:],
    )


def get_basin_neighbors(i, j, data, i_max, j_max, basin_points):
    if i < i_max - 1 and data[i + 1][j] < 9:
        if (i + 1, j, data[i + 1][j]) not in basin_points:
            basin_points.add((i + 1, j, data[i + 1][j]))
            get_basin_neighbors(i + 1, j, data, i_max, j_max, basin_points)

    if i > 0 and data[i - 1][j] < 9:
        if (i - 1, j, data[i - 1][j]) not in basin_points:
            basin_points.add((i - 1, j, data[i - 1][j]))
            get_basin_neighbors(i - 1, j, data, i_max, j_max, basin_points)

    if j < j_max - 1 and data[i][j + 1] < 9:
        if (i, j + 1, data[i][j + 1]) not in basin_points:
            basin_points.add((i, j + 1, data[i][j + 1]))
            get_basin_neighbors(i, j + 1, data, i_max, j_max, basin_points)

    if j > 0 and data[i][j - 1] < 9:
        if (i, j - 1, data[i][j - 1]) not in basin_points:
            basin_points.add((i, j - 1, data[i][j - 1]))
            get_basin_neighbors(i, j - 1, data, i_max, j_max, basin_points)
    return basin_points
