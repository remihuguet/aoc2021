import origami

test_input = "13/test_input.txt"


def test_parse_input():

    assert (
        [
            (6, 10),
            (0, 14),
            (9, 10),
            (0, 3),
            (10, 4),
            (4, 11),
            (6, 0),
            (6, 12),
            (4, 1),
            (0, 13),
            (10, 12),
            (3, 4),
            (3, 0),
            (8, 4),
            (1, 10),
            (2, 14),
            (8, 10),
            (9, 0),
        ],
        [("y", 7), ("x", 5)],
    ) == origami.parse_input(test_input)


def test_compute_dots_after_folds():
    points, folds = origami.parse_input(test_input)
    assert 17 == len(origami._apply_fold(dots=set(points), fold=folds[0]))


def test_transform_to_grid():
    assert [
        "#####",
        "#...#",
        "#...#",
        "#...#",
        "#####",
    ] == origami.transform_to_grid(origami.compute_dots_after_folds(test_input))
