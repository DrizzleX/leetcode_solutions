#!/bin/env python
class Solution:
    def hammingWeight(self, n):
        """
        >>> solution = Solution()
        >>> solution.hammingWeight(3)
        2
        """
        cnt = 0
        while n:
            cnt += (n & 1)
            n >>= 1
        return cnt

    def hammingWeight_use_bin(self, n):
        """
        >>> solution = Solution()
        >>> solution.hammingWeight(3)
        2
        """
        return bin(n).count('1')
        
