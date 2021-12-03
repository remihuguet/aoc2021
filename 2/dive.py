def read_input(input_file):
    with open(input_file, 'r') as f:
        return [i for i in f.readlines()]

def compute_final_position(input_file):
    h, d = 0, 0
    instructions = read_input(input_file)
    for inst in instructions:
        match inst.split(' '):
            case ["forward", n]:
                h += int(n)
            case ["down", n]:
                d += int(n)
            case ["up", n]:
                d -= int(n)
    return h * d


def compute_final_position_with_aim(input_file):
    h, d, aim = 0, 0, 0
    instructions = read_input(input_file)
    for inst in instructions:
        match inst.split(' '):
            case ["forward", n]:
                h += int(n)
                d += int(n) * aim
            case ["down", n]:
                aim += int(n)
            case ["up", n]:
                aim -= int(n)
    return h * d