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


def decode_wiring(input: str):
    patterns, output = parse_segment(input)
    wiring = {
        "a": None,
        "b": None,
        "c": None,
        "d": None,
        "e": None,
        "f": None,
        "g": None,
    }
    one = list(filter(lambda x: len(x) == 2, patterns))[0]
    wiring["c"] = one[0]
    wiring["f"] = one[1]

    seven = list(filter(lambda x: len(x) == 3, patterns))[0]
    wiring["a"] = seven[0]

    eight = list(filter(lambda x: len(x) == 7, patterns))[0]

    lensix = list(filter(lambda x: len(x) == 6, patterns))
    lenfive = list(filter(lambda x: len(x) == 5, patterns))

    setlensix = [
        set(el) - set([wiring["a"], wiring["c"], wiring["f"]]) for el in lensix
    ]
    setlenfive = [
        set(el) - set([wiring["a"], wiring["c"], wiring["f"]]) for el in lenfive
    ]

    setsix = list(filter(lambda x: len(x) == 4, setlensix))
    setthree = list(filter(lambda x: len(x) == 2, setlenfive))
    six = lensix[setlensix.index(setsix[0])]
    three = lenfive[setlenfive.index(setthree[0])]
    print(setlenfive)
    print(six, three)
