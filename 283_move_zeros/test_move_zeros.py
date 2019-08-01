import pytest
from move_zeros import Solution

test_data_set = [
    ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
    ([0, 0], [0, 0]),
    ([1, 0], [1, 0]),
    ([0, 1], [1, 0]),
    ([0, 1, 1, 0, 0, 3, 0, 2], [1, 1, 3, 2, 0, 0, 0, 0]),
    ([0], [0]),
    ([1], [1]),
    ([2, 1], [2, 1]),
    ([2, 1, 3], [2, 1, 3]),
    ([2, 1, 0, 3], [2, 1, 3, 0]),
    ([2, 1, 3, 0], [2, 1, 3, 0]),
]

@pytest.mark.parametrize("nums, expected", test_data_set)
def test_solution(nums, expected):
    solution = Solution()
    solution.moveZeroes(nums)
    assert nums == expected

