from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        We need a p1 to find the next zero, and a p2 to find the next non-zero
        """
        n = len(nums)
        if n <= 1:
            return None
        
        # only 2 or more numbers are meaningful
        
        p1, p2 = 0, 1
        while True:
            while p1 <= n-1 and nums[p1] != 0:
                # Find the next zero
                p1 += 1
            while p2 < p1 or (p2 <= n-1 and nums[p2] == 0):
                # Find the next non-zero
                p2 += 1
            if p2 == n:
                break
            else:
                nums[p1], nums[p2] = nums[p2], nums[p1]
                p1 += 1