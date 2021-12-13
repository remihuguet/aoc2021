def read_input(input_file):
    with open(input_file, "r") as f:
        return [i for i in f.readlines()]


def _read_state(input_file):
    inputs = read_input(input_file)
    state = [line.replace("\n", "") for line in inputs]
    return [[int(i) for i in line] for line in state]


def compute_flash_after_steps(input_file, steps):
    state = _read_state(input_file)
    flash = 0
    for _ in range(steps):
        state = next_step(state)
        flash += len([i for line in state for i in line if i == 0])
    return flash


def compute_step_big_flash(input_file):
    state = _read_state(input_file)
    n_octo = len(state) * len(state[0])
    flash = 0
    steps = 0
    while flash < n_octo:
        steps += 1
        state = next_step(state)
        flash = len([i for line in state for i in line if i == 0])
    return steps


def next_step(state):
    i_max, j_max = len(state) - 1, len(state[0]) - 1

    next_state = [[i + 1 for i in line] for line in state]
    flashed = set()
    for i, line in enumerate(next_state):
        for j, _ in enumerate(line):
            _flash(i, j, i_max, j_max, flashed, next_state)

    state = [[0 if v > 9 else v for v in line] for line in next_state]
    return state


def _flash(i, j, i_max, j_max, flashed, next_state):
    if next_state[i][j] > 9 and (i, j) not in flashed:
        flashed.add((i, j))
        if i < i_max:
            next_state[i + 1][j] += 1
            _flash(i + 1, j, i_max, j_max, flashed, next_state)
        if j < j_max:
            next_state[i][j + 1] += 1
            _flash(i, j + 1, i_max, j_max, flashed, next_state)
        if i < i_max and j < j_max:
            next_state[i + 1][j + 1] += 1
            _flash(i + 1, j + 1, i_max, j_max, flashed, next_state)
        if j > 0:
            next_state[i][j - 1] += 1
            _flash(i, j - 1, i_max, j_max, flashed, next_state)
        if i < i_max and j > 0:
            next_state[i + 1][j - 1] += 1
            _flash(i + 1, j - 1, i_max, j_max, flashed, next_state)
        if i > 0:
            next_state[i - 1][j] += 1
            _flash(i - 1, j, i_max, j_max, flashed, next_state)
        if i > 0 and j < j_max:
            next_state[i - 1][j + 1] += 1
            _flash(i - 1, j + 1, i_max, j_max, flashed, next_state)
        if i > 0 and j > 0:
            next_state[i - 1][j - 1] += 1
            _flash(i - 1, j - 1, i_max, j_max, flashed, next_state)
