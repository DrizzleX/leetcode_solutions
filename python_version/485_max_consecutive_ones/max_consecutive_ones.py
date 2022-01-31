import pytest
from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        count = 0
        max_count = 0
        for each in nums:
            if each == 1:
                count += 1
            else:
                max_count = count if count > max_count else max_count
                count = 0
        
        max_count = count if count > max_count else max_count

        return max_count



test_data_set = [
]


@pytest.mark.parametrize('', test_data_set)
def test_solution():
    solution = Solution()
        