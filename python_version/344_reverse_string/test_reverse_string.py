import pytest
from reverse_string import Solution

test_data_set = [
    ("asdf", "fdsa"),
    ("abc", "cba"),
    ("a", "a"),
    ('', '')
]

@pytest.mark.parametrize("s, expected", test_data_set)
def test_solution(s, expected):
    solution = Solution()
    lst_s = list(s)
    solution.reverseString(lst_s)
    assert ''.join(lst_s) == expected