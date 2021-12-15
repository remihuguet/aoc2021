from collections import defaultdict
import chiton

test_input = "15/test_input.txt"


def test_parse_input():
    assert chiton.parse_input(test_input) == [
        [1, 1, 6, 3, 7, 5, 1, 7, 4, 2],
        [1, 3, 8, 1, 3, 7, 3, 6, 7, 2],
        [2, 1, 3, 6, 5, 1, 1, 3, 2, 8],
        [3, 6, 9, 4, 9, 3, 1, 5, 6, 9],
        [7, 4, 6, 3, 4, 1, 7, 1, 1, 1],
        [1, 3, 1, 9, 1, 2, 8, 1, 3, 7],
        [1, 3, 5, 9, 9, 1, 2, 4, 2, 1],
        [3, 1, 2, 5, 4, 2, 1, 6, 3, 9],
        [1, 2, 9, 3, 1, 3, 8, 5, 2, 1],
        [2, 3, 1, 1, 9, 4, 4, 5, 8, 1],
    ]


def test_build_graph():
    map = [
        [1, 1, 6],
        [1, 3, 8],
        [2, 1, 3],
    ]

    assert {
        (0, 0): {(0, 1): 1, (1, 0): 1},
        (0, 1): {(0, 0): 1, (1, 1): 3, (0, 2): 6},
        (0, 2): {(0, 1): 1, (1, 2): 8},
        (1, 0): {(0, 0): 1, (2, 0): 2, (1, 1): 3},
        (1, 1): {(1, 0): 1, (1, 2): 8, (0, 1): 1, (2, 1): 1},
        (1, 2): {(1, 1): 3, (0, 2): 6, (2, 2): 3},
        (2, 0): {(1, 0): 1, (2, 1): 1},
        (2, 1): {(2, 0): 2, (2, 2): 3, (1, 1): 3},
        (2, 2): {(2, 1): 1, (1, 2): 8},
    } == chiton.build_graph(map)


def test_get_lowest_risk_path():
    assert 40 == chiton.get_lowest_risk_path(test_input)


def test_generate_map():
    map = [[8]]
    assert [
        [8, 9, 1, 2, 3],
        [9, 1, 2, 3, 4],
        [1, 2, 3, 4, 5],
        [2, 3, 4, 5, 6],
        [3, 4, 5, 6, 7],
    ] == chiton.generate_map(map)
    map = [[8, 1], [1, 2]]
    assert [
        [8, 1, 9, 2, 1, 3, 2, 4, 3, 5],
        [1, 2, 2, 3, 3, 4, 4, 5, 5, 6],
        [9, 2, 1, 3, 2, 4, 3, 5, 4, 6],
        [2, 3, 3, 4, 4, 5, 5, 6, 6, 7],
        [1, 3, 2, 4, 3, 5, 4, 6, 5, 7],
        [3, 4, 4, 5, 5, 6, 6, 7, 7, 8],
        [2, 4, 3, 5, 4, 6, 5, 7, 6, 8],
        [4, 5, 5, 6, 6, 7, 7, 8, 8, 9],
        [3, 5, 4, 6, 5, 7, 6, 8, 7, 9],
        [5, 6, 6, 7, 7, 8, 8, 9, 9, 1],
    ] == chiton.generate_map(map)


def test_get_lowest_risk_path_complete_map():
    assert 315 == chiton.get_lowest_risk_path_with_complete_map(test_input)
