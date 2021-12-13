import pathing

test_input = "12/test_input.txt"


def test_parse_input():
    assert {
        "start": {"A", "b"},
        "end": {"A", "b"},
        "c": {"A"},
        "A": {"start", "end", "c", "b"},
        "b": {"start", "end", "d", "A"},
        "d": {"b"},
    } == pathing.parse_input(test_input)


def test_build_paths():
    paths = pathing.build_paths(pathing.parse_input(test_input))

    assert (
        sorted(
            [
                ["start", "A", "b", "A", "c", "A", "end"],
                ["start", "A", "b", "A", "end"],
                ["start", "A", "b", "end"],
                ["start", "A", "c", "A", "b", "A", "end"],
                ["start", "A", "c", "A", "b", "end"],
                ["start", "A", "c", "A", "end"],
                ["start", "A", "end"],
                ["start", "b", "A", "c", "A", "end"],
                ["start", "b", "A", "end"],
                ["start", "b", "end"],
            ]
        )
        == sorted(paths)
    )


def test_count_paths():
    paths = pathing.parse_input(test_input)
    assert 10 == pathing.count_paths(paths)
    assert 36 == pathing.count_paths(paths, authorized_sc_twice=1)

    assert 19 == pathing.count_paths(
        pathing._build_data_dict(
            [
                "dc-end",
                "HN-start",
                "start-kj",
                "dc-start",
                "dc-HN",
                "LN-dc",
                "HN-end",
                "kj-sa",
                "kj-HN",
                "kj-dc",
            ]
        )
    )

    assert 103 == pathing.count_paths(
        pathing._build_data_dict(
            [
                "dc-end",
                "HN-start",
                "start-kj",
                "dc-start",
                "dc-HN",
                "LN-dc",
                "HN-end",
                "kj-sa",
                "kj-HN",
                "kj-dc",
            ]
        ),
        authorized_sc_twice=1,
    )

    assert 226 == pathing.count_paths(
        pathing._build_data_dict(
            [
                "fs-end",
                "he-DX",
                "fs-he",
                "start-DX",
                "pj-DX",
                "end-zg",
                "zg-sl",
                "zg-pj",
                "pj-he",
                "RW-he",
                "fs-DX",
                "pj-RW",
                "zg-RW",
                "start-pj",
                "he-WI",
                "zg-he",
                "pj-fs",
                "start-RW",
            ]
        )
    )

    assert 3509 == pathing.count_paths(
        pathing._build_data_dict(
            [
                "fs-end",
                "he-DX",
                "fs-he",
                "start-DX",
                "pj-DX",
                "end-zg",
                "zg-sl",
                "zg-pj",
                "pj-he",
                "RW-he",
                "fs-DX",
                "pj-RW",
                "zg-RW",
                "start-pj",
                "he-WI",
                "zg-he",
                "pj-fs",
                "start-RW",
            ]
        ),
        authorized_sc_twice=1,
    )
