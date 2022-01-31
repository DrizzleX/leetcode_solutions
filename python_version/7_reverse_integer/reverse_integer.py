import pytest



class Solution:
    def reverse(self, x: int) -> int:
        pass

    def reverseSimpleButWrong(self, x: int) -> int:
        # Simple solution that can pass, but does not meat criteria 
        if x < 0:
            is_negtive = True
            # -x can be greater than 32 bit signed integer, which violates the limit
            x = -x
        else:
            is_negtive = False

        result = 0
        while x:
            digit = x % 10
            result = result * 10 + digit
            x //= 10
        
        if not -(2**31) <= result <= 2**31-1:
            result = 0
        if is_negtive:
            result = -result

        return result





test_data_set = [
    (123, 321),
    (120, 21),
    (0, 0),
    (1, 1),
    (2**31-1, 0),
    (-1, -1),
    (-123, -321),
    (-120, -21),
]


@pytest.mark.parametrize('num, expected', test_data_set)
def test_solution(num, expected):
    solution = Solution()
    assert solution.reverse(num) == expected
        