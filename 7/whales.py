import statistics


def read_input(input_file):
    with open(input_file, "r") as f:
        return [i for i in f.readlines()]


def compute_optimal_position_fuel(input_file: str):
    positions = [int(i) for i in read_input(input_file)[0].split(",")]
    median = int(statistics.median(positions))

    return sum([abs(i - median) for i in positions])


def compute_optimal_position_fuel_2(input_file: str):
    positions = [int(i) for i in read_input(input_file)[0].split(",")]
    mean = int(statistics.mean(positions))
    candidates = range(round(mean - abs(mean / 10)), round(mean + abs(mean / 10)) + 2)
    f = []
    for c in candidates:
        f.append(sum([sum([j for j in range(1, abs(i - c) + 1)]) for i in positions]))
    return min(f)
