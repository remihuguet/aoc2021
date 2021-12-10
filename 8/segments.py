from itertools import permutations


def read_input(input_file):
    with open(input_file, "r") as f:
        return [i for i in f.readlines()]


def parse_segment(input: str):
    return [tuple(l.split(" ")) for l in input.replace("\n", "").split(" | ")]


def get_numbers_of_unique_segments(input_file: str):
    lines = read_input(input_file)
    segments = [parse_segment(line) for line in lines]
    unique_digits_len = {2: 0, 3: 0, 4: 0, 7: 0}
    for segment in segments:
        for s in segment[1]:
            if len(s) in unique_digits_len:
                unique_digits_len[len(s)] += 1
    return sum(unique_digits_len.values())


numbers_repr = {
    0: "abcefg",
    1: "cf",
    2: "acdeg",
    3: "acdfg",
    4: "bcdf",
    5: "abdfg",
    6: "abdefg",
    7: "acf",
    8: "abcdefg",
    9: "abcdfg",
}


digits = [
    "abcefg",
    "cf",
    "acdeg",
    "acdfg",
    "bcdf",
    "abdfg",
    "abdefg",
    "acf",
    "abcdefg",
    "abcdfg",
]


def decode_wiring(input: str):
    patterns, _ = parse_segment(input)

    for permutation in permutations("abcdefg"):
        if all(decode(pattern, permutation) in digits for pattern in patterns):
            break
    return "".join(permutation)


def decode(pattern: str, permutation: tuple):
    perm = "".join(permutation)
    decoded = []
    for p in pattern:
        decoded.append(chr(perm.index(p) + ord("a")))
    decoded.sort()
    return "".join(decoded)


def decode_output(input: str):
    wiring = decode_wiring(input)
    _, outputs = parse_segment(input)
    return [digits.index(decode(output, wiring)) for output in outputs]


def compute_score(input_file: str):
    lines = read_input(input_file)
    scores = [int("".join(map(str, decode_output(line)))) for line in lines]
    return sum(int(s) for s in scores)
