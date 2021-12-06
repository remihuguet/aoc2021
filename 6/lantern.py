def read_input(input_file):
    with open(input_file, "r") as f:
        return [i for i in f.readlines()]


def tick(state: dict) -> dict:
    new_state = {k: 0 for k in range(9)}
    new_state[8] = new_state[6] = state[0]
    for i in range(0, 8):
        new_state[i] += state[i + 1]
    return new_state


def _transform_state(initial_state: list) -> dict:
    state = {k: 0 for k in range(9)}
    for s in initial_state:
        state[int(s)] += 1
    return state


def compute_number_of_fish_after(input_file: str, days: int):
    initial_state = read_input(input_file)
    state = _transform_state(initial_state[0].split(","))

    for i in range(days):
        state = tick(state)
    return sum(state.values())
