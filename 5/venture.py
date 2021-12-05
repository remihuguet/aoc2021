def read_input(input_file):
    with open(input_file, "r") as f:
        return [i for i in f.readlines()]


def compute_overlapping_with_all(input_file: str):
    lines, x_max, y_max = _compute_lines(input_file, lambda s, e: True)

    return _compute_res_from_lines(lines, x_max, y_max)


def compute_overlapping_lines(input_file: str):
    lines, x_max, y_max = _compute_lines(
        input_file, lambda start, end: start[0] == end[0] or start[1] == end[1]
    )

    return _compute_res_from_lines(lines, x_max, y_max)


def _compute_lines(input_file: str, condition: callable):
    inputs = read_input(input_file)
    inputs = [line.replace("\n", "").split(" -> ") for line in inputs]

    x_max, y_max = 0, 0
    lines = []
    for line in inputs:
        start, end = (int(line[0].split(",")[0]), int(line[0].split(",")[1])), (
            int(line[1].split(",")[0]),
            int(line[1].split(",")[1]),
        )
        if condition(start, end):
            x_max, y_max = max(start[0], end[0], x_max), max(start[1], end[1], y_max)
            lines.append((start, end))

    return lines, x_max, y_max


def _compute_res_from_lines(lines: list, x_max: int, y_max: int):
    map = [[0 for i in range(x_max + 1)] for j in range(y_max + 1)]
    for line in lines:
        start, end = line[0], line[1]

        if start[0] == end[0]:
            x = start[0]
            y_range = range(*sorted([end[1], start[1]]))
            for y in y_range:
                map[y][x] += 1
            map[y_range[-1] + 1][x] += 1
        elif start[1] == end[1]:
            y = start[1]
            x_range = range(*sorted([end[0], start[0]]))
            for x in x_range:
                map[y][x] += 1
            map[y][x_range[-1] + 1] += 1
        else:
            x_start, x_end, x_dir = start[0], end[0], 1 if end[0] > start[0] else -1
            y_start, y_end, y_dir = start[1], end[1], 1 if end[1] > start[1] else -1

            if abs(x_end - x_start) != abs(y_end - y_start):
                raise Exception("Houston, we have a problem.")

            for i in range(abs(x_end - x_start) + 1):
                map[y_start + y_dir * i][x_start + x_dir * i] += 1

    res = 0
    for line in map:
        for col in line:
            if col > 1:
                res += 1
    return res
