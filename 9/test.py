import smoke


input_file = "9/test_input.txt"


def test_find_minima():
    assert smoke.find_minima(input_file)[0] == set(
        [(0, 9, 0), (0, 1, 1), (2, 2, 5), (4, 6, 5)]
    )


def test_compute_risk():
    assert smoke.compute_risk(input_file) == 15


def test_compute_size_of_basin():
    assert smoke.compute_size_of_basins(input_file) == 1134
