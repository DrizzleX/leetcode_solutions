#!/bin/env python
import pytest
from majority_element import Solution

test_data_set = [
    ([3, 1, 3], 3),
    ([2, 2, 1, 1, 1, 2, 2], 2),
    ([2, 1, 1, 2, 2], 2),
]

@pytest.mark.parametrize("nums, expected", test_data_set)
def test_solution(nums, expected):
    solution = Solution()
    assert solution.majorityElement(nums) == expected
        