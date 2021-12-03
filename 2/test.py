import dive


input_file = '2/test_input.txt'


def test_compute_final_position():
    expected = 150
    assert expected == dive.compute_final_position(input_file)

def test_compute_final_position_with_aim():
    expected = 900
    assert expected == dive.compute_final_position_with_aim(input_file)
