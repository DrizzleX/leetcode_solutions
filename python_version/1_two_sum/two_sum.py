from typing import List
import pytest


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}
        for idx, num in enumerate(nums):
            other_num = target - num
            if other_num in num_to_index:
                # If other_num == num, return the idx for previous occurance and the current occurance
                # If other_num != num, return the indices of 2 different numbers
                return sorted([idx, num_to_index[other_num]])
            else:
                # we have not found the answer yet, save the idx for num
                num_to_index[num] = idx
        return None

    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        num_to_index = dict()
        for idx, num in enumerate(nums):
            if num not in num_to_index:
                num_to_index[num] = [idx]
            else:
                num_to_index[num].append(idx)

        for num, indices in num_to_index.items():
            other_num = target - num
            if other_num in num_to_index:
                if other_num == num:
                    if len(indices) == 2:
                        return indices
                else:
                    return [indices[0], num_to_index[other_num][0]]
        return None
    
    def twoSumRecordPositions(self, nums: List[int], target: int) -> List[int]:
        """
        Record the postions of all numbers
        """
        from collections import defaultdict
        # Each number can appear more than once, so we use a list to store its
        # occurances
        num_to_positions = defaultdict(list)
        for pos, val in enumerate(nums):
            num_to_positions[val].append(pos)
            
        for num, positions in num_to_positions.items():
            the_other_num = target - num
            if the_other_num in num_to_positions:
                the_other_positions = num_to_positions[the_other_num]
                if num == the_other_num:
                    # If the target CAN be composed of num * 2, e.g. ([3, 3, 1], 6)
                    if len(positions) > 1:
                        # num must appear 2 times because the same number can't
                        # be used twice.
                        # If it does, return the positions
                        # Since we know there is exactly 1 solution, we can safely return the positions
                        return the_other_positions
                    # We only have 1 num, and it can't be used more than once, so we continue searching
                    continue
                # number != the_other_num, we know this must be the only answer
                return [positions[0], the_other_positions[0]]

    def twoSum_O_N2(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return None
        

test_data_set = [
    ([2, 7, 11, 15], 9, [0, 1]),
    ([1, 2, 3, 4], 7, [2, 3]),
    ([9, 4, 2, 1], 10, [0, 3]),
    ([4, 3, 2, 8], 5, [1, 2]),
    ([3, 4, 2], 6, [1, 2]),
    ([3, 3], 6, [0, 1]),
    ([3, 4, 5, 6, 9, 10, 9, 3], 18, [4, 6]),
]

@pytest.mark.parametrize("nums, target, expected", test_data_set)
def test_twoSum(nums, target, expected):
    solution = Solution()
    result = solution.twoSum(nums, target)
    assert result == expected
