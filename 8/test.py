import segments


input_file = "8/test_input.txt"


def test_get_numbers_of_unique_segments():
    assert segments.get_numbers_of_unique_segments(input_file) == 26


def test_decode_wiring():
    input = "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"
    output = "deafgbc"
    assert output == segments.decode_wiring(input)


def test_decode_output_patterns():
    input = "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"
    assert [5, 3, 5, 3] == segments.decode_output(input)


def test_compute_score():
    assert 61229 == segments.compute_score(input_file)
