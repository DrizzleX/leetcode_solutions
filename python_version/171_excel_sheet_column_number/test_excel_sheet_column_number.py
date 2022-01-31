#!/bin/env python
import pytest
from excel_sheet_column_number import Solution

test_data_set = [
    ("A", 1),
    ("AB", 28),
    ("ZY", 701),
]

@pytest.mark.parametrize("title, expected", test_data_set)
def test_solution(title, expected):
    solution = Solution()
    assert solution.titleToNumber(title) == expected
        
