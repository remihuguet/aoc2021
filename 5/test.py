import venture


input_file = "5/test_input.txt"


def test_compute_overlapping_lines():
    assert 5 == venture.compute_overlapping_lines(input_file)


def test_compute_overlapping_with_all():
    assert 12 == venture.compute_overlapping_with_all(input_file)
