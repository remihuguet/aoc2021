import lantern


input_file = "6/test_input.txt"


def test_compute_fish_after_1_day():
    assert lantern._transform_state([2, 3, 2, 0, 1]) == lantern.tick(
        lantern._transform_state([3, 4, 3, 1, 2])
    )


def test_compute_fish_after_2_days():
    assert lantern._transform_state([1, 2, 1, 6, 0, 8]) == lantern.tick(
        lantern._transform_state([2, 3, 2, 0, 1])
    )


def test_compute_fish_after_3_days():
    assert lantern._transform_state([0, 1, 0, 5, 6, 7, 8]) == lantern.tick(
        lantern._transform_state([1, 2, 1, 6, 0, 8])
    )


def test_compute_number_of_fish_after_x_days():
    assert 26 == lantern.compute_number_of_fish_after(input_file, days=18)
    assert 5934 == lantern.compute_number_of_fish_after(input_file, days=80)


def test_compute_big_number():
    assert 26984457539 == lantern.compute_number_of_fish_after(input_file, days=256)
