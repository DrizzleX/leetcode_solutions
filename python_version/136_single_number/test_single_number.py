import pytest
from single_number import Solution

test_data_set = [
    ([1, 1, 2], 2),
    ([1, 1, 4, 4, 3, 5, 3], 5),
    ([4, 1, 2, 1, 2], 4),
]

@pytest.mark.parametrize("nums, expected", test_data_set)
def test_solution(nums, expected):
    solution = Solution()
    assert solution.singleNumber(nums) == expected

