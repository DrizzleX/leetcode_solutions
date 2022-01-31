import pytest
from pascal_triangle import Solution

test_data_set = [
    (
        1, [
            [1],
        ]),
    (
        2, [
            [1],
            [1, 1]
        ]
    ),
    (
        3, [
            [1],
            [1, 1],
            [1, 2, 1]
        ]
    ),
    (
        5, [
            [1],
            [1,1],
            [1,2,1],
            [1,3,3,1],
            [1,4,6,4,1]
        ]
    ),
]

@pytest.mark.parametrize("num_rows, expected", test_data_set)
def test_solution(num_rows, expected):
    solution = Solution()
    assert expected == solution.generate(num_rows)