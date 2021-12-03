def read_input(input_file):
    with open(input_file, "r") as f:
        return [i for i in f.readlines()]


def compute_rate(input_file: str):
    inputs = read_input(input_file)

    lines = [i.replace("\n", "") for i in inputs]

    most_commons = _compute_most_commons(lines)

    gamma, epsilon = "0b" + "".join(most_commons), "0b" + "".join(
        ["1" if c == "0" else "0" for c in most_commons]
    )
    return int(gamma, 2) * int(epsilon, 2)


def compute_co2_oxy(input_file: str):
    inputs = read_input(input_file)

    lines = [i.replace("\n", "") for i in inputs]

    co2_most_commons = _compute_most_commons(lines)
    co2_candidates = o2_candidates = lines

    for c in range(len(lines[0])):
        co2_most_commons = _compute_most_commons(co2_candidates)
        co2_candidates = [l for l in co2_candidates if l[c] == co2_most_commons[c]]
        if len(co2_candidates) == 1:
            break
    co2 = "0b" + "".join(co2_candidates[0])

    for c in range(len(lines[0])):
        o2_most_commons = _compute_most_commons(o2_candidates)
        o2_candidates = [l for l in o2_candidates if l[c] != o2_most_commons[c]]
        if len(o2_candidates) == 1:
            break

    o2 = "0b" + "".join(o2_candidates[0])
    return int(co2, 2) * int(o2, 2)


def _compute_most_commons(lines: list[str]):
    cols = [[] for i in range(len(lines[0]))]

    for k, col in enumerate(cols):
        for line in lines:
            col.append(line[k])

    most_commons = []
    for col in cols:
        count_1, count_0 = len([i for i in col if i == "1"]), len(
            [i for i in col if i == "0"]
        )
        most_commons.append("1" if count_1 >= count_0 else "0")
    return most_commons
