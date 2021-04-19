#!/bin/env python
import pytest
from valid_anagram import Solution

test_data_set = [
    ("abc", "xxb", False),
    ("abc", "cab", True),
]

@pytest.mark.parametrize("s, t, expected", test_data_set)
def test_solution(s, t, expected):
    solution = Solution()
    assert solution.isAnagram(s, t) == expected
        