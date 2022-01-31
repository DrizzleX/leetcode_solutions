import pytest


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching_pairs = {
            ')': '(',
            ']': '[',
            '}': '{',
        }
        for each in s:
            if each in matching_pairs:
                if not stack:
                    return False
                top = stack.pop()
                if top != matching_pairs[each]:
                    return False
            elif each in matching_pairs.values():
                stack.append(each)
        
        return True if not stack else False


test_data_set = [
    ('(', False),
    (')', False),
    ('((a+a) + b)', True),
    ('((a+) + b)', True),
]

@pytest.mark.parametrize("s, expected", test_data_set)
def test_solution(s, expected):
    solution = Solution()
    assert solution.isValid(s) == expected

