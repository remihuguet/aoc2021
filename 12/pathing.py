def read_input(input_file):
    with open(input_file, "r") as f:
        return [i for i in f.readlines()]


def parse_input(input_file: str) -> dict:
    data = read_input(input_file)
    return _build_data_dict(data)


def _build_data_dict(data):
    data_dict = {}

    for line in data:
        line = line.replace("\n", "")
        d1, d2 = line.split("-")
        if d1 not in data_dict:
            data_dict[d1] = set()
        if d2 not in data_dict:
            data_dict[d2] = set()
        data_dict[d1].add(d2)
        data_dict[d2].add(d1)
    return data_dict


def count_paths(paths, authorized_sc_twice=0) -> int:
    paths = build_paths(paths, authorized_sc_twice=authorized_sc_twice)
    return len(paths)


def build_paths(paths: dict, authorized_sc_twice=0) -> list:
    small_caves = [d for d in paths.keys() if d.islower()]
    return _compute_paths(["start"], paths, [], small_caves, authorized_sc_twice)


def _compute_paths(base_path, data_dict, paths, small_caves, authorized_sc_twice):
    for node in data_dict[base_path[-1]]:
        _path = base_path + [node]
        if node == "start":
            continue
        elif node == "end":
            paths.append(_path)
        else:
            small_caves_visits = [
                len([p for p in _path if p == c]) for c in small_caves
            ]
            if any([s > 2 for s in small_caves_visits]):
                continue
            elif len([s for s in small_caves_visits if s == 2]) > authorized_sc_twice:
                continue
            else:
                _compute_paths(
                    _path,
                    data_dict,
                    paths,
                    small_caves,
                    authorized_sc_twice=authorized_sc_twice,
                )
    return paths
