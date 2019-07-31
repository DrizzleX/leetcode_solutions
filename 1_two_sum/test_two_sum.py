import pytest
from two_sum import Solution

test_data_set = [
    ([2, 7, 11, 15], 9, [0, 1]),
    ([1, 2, 3, 4], 7, [2, 3]),
    ([9, 4, 2, 1], 10, [0, 3]),
    ([4, 3, 2, 8], 5, [1, 2]),
    ([3, 4, 2], 6, [1, 2]),
    ([3, 3], 6, [0, 1]),
    ([3, 4, 5, 6, 9, 10, 9, 3], 18, [4, 6]),
]

@pytest.mark.parametrize("nums, target, expected", test_data_set)
def test_twoSum(nums, target, expected):
    solution = Solution()
    result = solution.twoSum(nums, target)
    assert result == expected
