import pytest
from typing import List
from singly_linked_list import ListNode, make_linked_list, print_linked_list, linked_list_as_list


class Solution:
    def romanToInt(self, s: str) -> int:
        pass


test_data_set = [
    ('LVIII', 58)
]


@pytest.mark.parametrize('s, num', test_data_set)
def test_solution(s, num):
    solution = Solution()
    assert Solution.romanToInt(s) == num
        
