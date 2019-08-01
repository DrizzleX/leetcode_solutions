from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        """
        n = len(nums)
        if n <= 1:
            return None
        
        p1, p2 = 0, 1
        while True:
            while p1 <= n-1 and nums[p1] != 0:
                p1 += 1
            if p2 == p1:
            while p2 <= n-1 and nums[p2] == 0:
                p2 += 1
            if p2 == n:
                break
            nums[p1], nums[p2] = nums[p2], nums[p1]
            p1 += 1
