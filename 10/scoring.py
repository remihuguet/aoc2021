from functools import reduce


def read_input(input_file):
    with open(input_file, "r") as f:
        return [i for i in f.readlines()]


openings = ["[", "(", "{", "<"]
closings = ["]", ")", "}", ">"]

pairs = {"[": "]", "(": ")", "<": ">", "{": "}"}


def valid_pattern(pattern: str):
    return completion(pattern)


corrupts_scores = {")": 3, "]": 57, "}": 1197, ">": 25137}


def compute_syntax_error_score(input_file: str):
    lines = read_input(input_file)
    score = 0
    for line in lines:
        valid, char = valid_pattern(line)
        if not valid:
            score += corrupts_scores[char]
    return score


scorings = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}


def completion_score(comp: str):
    return reduce(lambda score, c: score * 5 + scorings[c], comp, 0)


def completion(pattern: str):
    opened = []
    for c in pattern:
        if c in closings:
            if not opened or opened[-1] != openings[closings.index(c)]:
                return False, c
            else:
                opened.pop()
        elif c in openings:
            opened.append(c)

    completion = []
    for c in reversed(opened):
        completion.append(pairs[c])
    return True, "".join(completion)


def get_completion_winner(input_file: str):
    lines = read_input(input_file)
    scores = []
    for line in lines:
        valid, comp = completion(line)
        if valid:
            scores.append(completion_score(comp))
    return sorted(scores)[len(scores) // 2]
