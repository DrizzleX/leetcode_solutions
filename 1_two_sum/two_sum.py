from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}
        for idx, num in enumerate(nums):
            other_num = target - num
            if other_num in num_to_index:
                return sorted([idx, num_to_index[other_num]])
            else:
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

    def twoSum_ON2(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return None
        