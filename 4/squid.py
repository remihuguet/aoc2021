def read_input(input_file):
    with open(input_file, "r") as f:
        return [i for i in f.readlines()]


def compute_winning_score(input_file: str):
    first_winning_board = _compute_winnings(input_file)[0]
    return sum([sum(line) for line in first_winning_board[1]]) * first_winning_board[0]


def compute_last_winning_score(input_file: str):
    winning_board = _compute_winnings(input_file)[-1]
    return sum([sum(line) for line in winning_board[1]]) * winning_board[0]


def _compute_winnings(input_file: str):
    inputs = read_input(input_file)

    draw = [int(i) for i in inputs[0].split(",")]

    boards = []
    k = -1
    for i in inputs[1:]:
        if i == "\n":
            k += 1
            boards.append([])
            continue
        else:
            boards[k].append(
                [int(j) for j in i.replace("\n", "").split(" ") if j != ""]
            )
    boards[-1].pop()

    boards_in_col = []
    for board in boards:
        board_in_col = [[] for i in range(5)]
        for i, line in enumerate(board):
            for k, col in enumerate(line):
                board_in_col[k].append(col)
        boards_in_col.append(board_in_col)

    winning_boards = []

    for d in draw:
        for k, board in enumerate(boards):
            for line in board:
                if d in line:
                    line.pop(line.index(d))
            for col in boards_in_col[k]:
                if d in col:
                    col.pop(col.index(d))
        for k, board in enumerate(boards):
            if any(len(l) == 0 for l in board) or any(
                len(c) == 0 for c in boards_in_col[k]
            ):
                winning_boards.append((d, board))
                boards.pop(k)
                boards_in_col.pop(k)
    return winning_boards
