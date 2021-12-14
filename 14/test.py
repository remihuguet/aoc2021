from collections import defaultdict
import polymerisation

test_input = "14/test_input.txt"


def test_parse_input():
    template, insertions = "NNCB", [
        ("CH", "B"),
        ("HH", "N"),
        ("CB", "H"),
        ("NH", "C"),
        ("HB", "C"),
        ("HC", "B"),
        ("HN", "C"),
        ("NN", "C"),
        ("BH", "H"),
        ("NC", "B"),
        ("NB", "B"),
        ("BN", "B"),
        ("BB", "N"),
        ("BC", "B"),
        ("CC", "N"),
        ("CN", "C"),
    ]
    assert template, insertions == polymerisation.parse_input(test_input)


def test_apply_insertions():
    template, insertions = polymerisation.parse_input(test_input)
    pairs = polymerisation.trans_template(template)

    assert polymerisation.trans_template("NCNBCHB") == polymerisation.apply_insertions(
        pairs, insertions
    )

    assert polymerisation.trans_template(
        "NBCCNBBBCBHCB"
    ) == polymerisation.apply_insertions(
        polymerisation.trans_template("NCNBCHB"), insertions
    )

    assert polymerisation.trans_template(
        "NBBBCNCCNBBNBNBBCHBHHBCHB"
    ) == polymerisation.apply_insertions(
        polymerisation.trans_template("NBCCNBBBCBHCB"), insertions
    )

    assert polymerisation.trans_template(
        "NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB"
    ) == polymerisation.apply_insertions(
        polymerisation.trans_template("NBBBCNCCNBBNBNBBCHBHHBCHB"), insertions
    )


def test_count_elements_after_steps():
    template, insertions = polymerisation.parse_input(test_input)

    counts = polymerisation.count_elements_after_steps(
        pairs=polymerisation.trans_template(template), insertions=insertions, steps=10
    )
    assert counts.most_common() == [
        ("B", 1748),
        ("N", 865),
        ("C", 298),
        ("H", 161),
    ]


def test_compute_result():
    assert 1588 == polymerisation.compute_result(test_input)


def test_compute_long_result():
    assert 2188189693529 == polymerisation.compute_result(test_input, steps=40)
