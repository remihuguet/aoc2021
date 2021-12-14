from collections import defaultdict
from typing import Counter


def read_input(input_file):
    with open(input_file, "r") as f:
        return [i for i in f.readlines()]


def parse_input(input_file: str):
    data = read_input(input_file)
    template = data[0].replace("\n", "")
    insertions = [line.replace("\n", "").split(" -> ") for line in data[2:]]
    return template, insertions


def apply_insertions(pairs, insertions: list):
    new_pairs = pairs.copy()
    for insertion in insertions:
        if insertion[0] in pairs:
            new_pairs[insertion[0]] -= pairs[insertion[0]]
            new_pairs[insertion[0][0] + insertion[1]] += pairs[insertion[0]]
            new_pairs[insertion[1] + insertion[0][1]] += pairs[insertion[0]]
            if new_pairs[insertion[0]] == 0:
                del new_pairs[insertion[0]]
    return new_pairs


def count_elements_after_steps(pairs, insertions, steps):
    for _ in range(steps):
        pairs = apply_insertions(pairs, insertions)

    letters = defaultdict(int)
    for k, v in pairs.items():
        letters[k[0]] += v
    return Counter(letters)


def compute_result(input_file, steps=10):
    template, insertions = parse_input(input_file)
    pairs = trans_template(template)
    counts = count_elements_after_steps(pairs, insertions, steps)
    counts[template[-1]] += 1
    return counts.most_common()[0][1] - counts.most_common()[-1][1]


def trans_template(template):
    pairs = defaultdict(int)
    for l, r in zip(template[:-1], template[1:]):
        pairs[l + r] += 1
    return pairs
