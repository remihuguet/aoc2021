import diagnostic


input_file = "3/test_input.txt"


def test_compute_gamma_and_epsilon():
    assert 198 == diagnostic.compute_rate(input_file)


def test_compute_co2_and_oxygen():
    assert 230 == diagnostic.compute_co2_oxy(input_file)
