#!/bin/env python
import pytest
from power_of_three import Solution

test_data_set = [
    (0, False),
    (1, True),
    (3, True),
    (4, False),
    (6, False),
    (9, True),
]

@pytest.mark.parametrize("num, expected", test_data_set)
def test_solution(num, expected):
    solution = Solution()
    assert solution.isPowerOfThree(num) == expected
        