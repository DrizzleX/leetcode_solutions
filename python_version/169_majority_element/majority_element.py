#!/bin/env python
from typing import List
from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]

    def majorityElement_vote(self, nums: List[int]) -> int:
        """
        Go through the list:
        majority_cnt == 0 -> we don't have any idea which number is the majority, so we will go with the current one
        majority_num == num -> current number is the same as the majority number, we increase our confidence about this majority number by +1
        majority_num != num -> we have a different voice, telling us there are other numbers, therefore we reduce our confidence about this majority number by -1
        """
        majority_num, majority_cnt = 0, 0
        for num in nums:
            if majority_cnt == 0:
                majority_num = num
            majority_cnt += (1 if majority_num == num else -1)
        return majority_num

    def majorityElement_defaultdict(self, nums: List[int]) -> int:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        for num, appearance in count.items():
            if appearance > len(nums)/2:
                return num
        