import squid


input_file = "4/test_input.txt"


def test_compute_winnining_score():
    assert squid.compute_winning_score(input_file) == 4512


def test_compute_last_winning_score():
    assert squid.compute_last_winning_score(input_file) == 1924
