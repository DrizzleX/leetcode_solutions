import random


def generate_input():
    MAX_COUNT = 2000
    long_list = [random.randint(1, MAX_COUNT) for each in range(MAX_COUNT)]
    lists = [
        (None, None),
        ([], []),
        ([3, 2, 1], [1, 2, 3]),
        ([3], [3]),
        (long_list, sorted(long_list)),
    ]
    return lists
