def read_input(input_file):
    with open(input_file, "r") as f:
        return [i for i in f.readlines()]


def parse_input(input_file: str):
    inputs = read_input(input_file)
    points, folds = [], []
    for line in inputs:
        if line[0] == "f":
            folds.append(tuple([line[11], int(line[13:])]))
        elif len(line) > 1:
            points.append(tuple([int(l) for l in line.replace("\n", "").split(",")]))
    return (points, folds)


def compute_dots_after_folds(input_file: str):
    points, folds = parse_input(input_file)
    dots = set(points)
    for f in folds:
        dots = _apply_fold(f, dots)
    return dots


def transform_to_grid(dots: set):
    x_max, y_max = 0, 0
    for dot in dots:
        x_max = max(dot[0], x_max)
        y_max = max(dot[1], y_max)

    grid = [["." for _ in range(x_max + 1)] for y in range(y_max + 1)]
    for dots in dots:
        grid[dots[1]][dots[0]] = "#"
    return ["".join(row) for row in grid]


def _apply_fold(fold, dots: set[tuple]):
    axis, value = fold
    res = set()
    if axis == "x":
        for dot in dots:
            if dot[0] - value > 0:
                res.add((2 * value - dot[0], dot[1]))
            else:
                res.add(dot)
    elif axis == "y":
        for dot in dots:
            if dot[1] - value > 0:
                res.add((dot[0], 2 * value - dot[1]))
            else:
                res.add(dot)
    return res
