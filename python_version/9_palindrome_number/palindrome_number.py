import pytest



class Solution:
    def isPalindrome(self, x: int) -> bool:
        # O(N), O(N)
        if x < 0:
            return False
        x_str = str(x)
        len_x_str = len(x_str)
        mid_idx = len_x_str // 2
        for i in range(len_x_str):
            if i == mid_idx:
                # We have gone through the first half.
                # For number with odd number of digits, e.g. 121, we are pointing at the middle (2)
                # For number with even number of digits, e.g. 1221, we are pointing at 1 past the middle (the 2nd 2)
                break
            j = len_x_str - i - 1
            if x_str[i] != x_str[j]:
                return False
        return True

    def isPalindromeNoConversion(self, x: int) -> bool:
        # O(log10(n)), O(1)
        if x < 0:
            return False
        reversed_second_half = 0
        while reversed_second_half < x:
            digit = x % 10
            reversed_second_half = reversed_second_half * 10 + digit
            if reversed_second_half == x:
                # If we have a palindrome number with odd number of digits, we will get here
                return True
            x //= 10
        return x == reversed_second_half


test_data_set = [
    (-1, False),
    (0, True),
    (12, False),
    (11, True),
    (122, False),
    (121, True),
    (12321, True),
    (1221, True),
    (1223, False),
]


@pytest.mark.parametrize('x, expected', test_data_set)
def test_solution(x, expected):
    solution = Solution()
    assert expected == solution.isPalindromeNoConversion(x)

        