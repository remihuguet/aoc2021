import sonar_sweep


input_file = '1/test_input.txt'


def test_depth_measurement_increases():
    expected = 7
    assert expected == sonar_sweep.depth_measurements_increase(input_file)


def test_depth_measurement_sliding_window():
    expected = 5
    assert expected == sonar_sweep.depth_measurements_sliding_windows_increase(input_file)