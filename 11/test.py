import octopus


def test_next_step():
    input = [
        [1, 1, 1, 1, 1],
        [1, 9, 9, 9, 1],
        [1, 9, 1, 9, 1],
        [1, 9, 9, 9, 1],
        [1, 1, 1, 1, 1],
    ]
    step1 = [
        [3, 4, 5, 4, 3],
        [4, 0, 0, 0, 4],
        [5, 0, 0, 0, 5],
        [4, 0, 0, 0, 4],
        [3, 4, 5, 4, 3],
    ]
    step2 = [
        [4, 5, 6, 5, 4],
        [5, 1, 1, 1, 5],
        [6, 1, 1, 1, 6],
        [5, 1, 1, 1, 5],
        [4, 5, 6, 5, 4],
    ]
    assert octopus.next_step(input) == step1
    assert octopus.next_step(step1) == step2


def test_compute_flash_after_steps():
    assert 204 == octopus.compute_flash_after_steps("11/test_input.txt", 10)
    assert 1656 == octopus.compute_flash_after_steps("11/test_input.txt", 100)


def test_step_big_flash():
    assert 195 == octopus.compute_step_big_flash("11/test_input.txt")
