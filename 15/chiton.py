from collections import defaultdict
import heapq


def read_input(input_file):
    with open(input_file, "r") as f:
        return [i for i in f.readlines()]


def parse_input(input_file: str):
    return [[int(i) for i in line.replace("\n", "")] for line in read_input(input_file)]


def generate_map(map):
    y_final, x_final = len(map) * 5 - 1, len(map[0]) * 5 - 1
    final_map = [[0 for _ in range(x_final + 1)] for _ in range(y_final + 1)]
    for y, row in enumerate(final_map):
        for x, _ in enumerate(row):
            qx, rx = divmod(x, len(map[0]))
            qy, ry = divmod(y, len(map))
            val = map[ry][rx] + qx + qy
            final_map[y][x] = val if val < 10 else val - 9
    return final_map


def build_graph(map):
    graph = defaultdict(dict)
    for y, row in enumerate(map):
        for x, _ in enumerate(row):
            if y > 0:
                graph[(y, x)][(y - 1, x)] = map[y - 1][x]
            if x > 0:
                graph[(y, x)][(y, x - 1)] = map[y][x - 1]
            if y < len(map) - 1:
                graph[(y, x)][(y + 1, x)] = map[y + 1][x]
            if x < len(row) - 1:
                graph[(y, x)][(y, x + 1)] = map[y][x + 1]
    return graph


def get_lowest_risk_path(input_file: str):
    map = parse_input(input_file)
    return _compute_lowest_path(map)


def _compute_lowest_path(map):
    target = (len(map) - 1, len(map[0]) - 1)
    graph = build_graph(map)

    distances = {vertex: float("inf") for vertex in graph}
    distances[(0, 0)] = 0

    pq = [(0, (0, 0))]
    while len(pq) > 0:
        current_distance, current_vertex = heapq.heappop(pq)
        if current_distance > distances[current_vertex]:
            continue

        if current_vertex == target:
            break
        for neighbor, weight in graph[current_vertex].items():
            new_distance = current_distance + weight

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(pq, (new_distance, neighbor))
    return distances[target]


def get_lowest_risk_path_with_complete_map(input_file):
    map = generate_map(parse_input(input_file))
    return _compute_lowest_path(map)
