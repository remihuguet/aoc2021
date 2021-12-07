import whales


input_file = "7/test_input.txt"


def test_compute_optimal_position_fuel():
    assert 37 == whales.compute_optimal_position_fuel(input_file)


def test_compute_optimal_position_fuel_2():
    assert 168 == whales.compute_optimal_position_fuel_2(input_file)
