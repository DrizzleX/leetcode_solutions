from typing import List
import pytest


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # O(N), O(N)
        max_number = len(nums)
        num_occurance = {num: 0 for num in range(1, max_number+1)}
        for num in nums:
            num_occurance[num] += 1
        result = {}
        for num, occurance in num_occurance.items():
            if occurance == 2:
                result['duplicate'] = num
            elif occurance == 0:
                result['missing'] = num
        return [result['duplicate'], result['missing']]
    
    def findErrorNumsSingleLoop(self, nums: List[int]) -> List[int]:
        # O(N), O(N)
        num_occurance = {}
        for num in nums:
            num_occurance.setdefault(num, 0)
            num_occurance[num] += 1
            if num_occurance[num] == 2:
                duplicate = num
                break
        missing = sum(range(1, len(nums)+1)) - sum(nums) + duplicate
        return [duplicate, missing]


test_data_set = [
    ([2, 2], [2, 1]),
    ([1, 2, 2, 4], [2, 3]),
    ([1, 4, 2, 2], [2, 3]),
    ([1, 2, 2, 3, 4, 5, 6], [2, 7]),
    ([1, 3, 4, 4, 5, 6], [4, 2]),
    ([1, 1], [1, 2]),
]


@pytest.mark.parametrize('nums, expected', test_data_set)
def test_solution(nums, expected):
    solution = Solution()
    assert solution.findErrorNumsSingleLoop(nums) == expected
        