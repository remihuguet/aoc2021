def read_input(input_file):
    with open(input_file, 'r') as f:
        return [i for i in f.readlines()]

def depth_measurements_increase(input_file):
    numbers = [int(i) for i in read_input(input_file)]
    diffs = [i - numbers[k-1] for k, i in enumerate(numbers) if k > 0]
    return len([i for i in diffs if i > 0])

def depth_measurements_sliding_windows_increase(input_file):
    numbers = [int(i) for i in read_input(input_file)]
    win_sums = [i+numbers[k+1]+numbers[k+2] for k, i in enumerate(numbers) if k < len(numbers)-2]
    diffs = [i - win_sums[k-1] for k, i in enumerate(win_sums) if k > 0]
    return len([i for i in diffs if i > 0])