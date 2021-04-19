from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for idx, num in enumerate(nums):
            if idx == 0:
                result = num
            else:
                result ^= num
        return result

    def singleNumber_record_occurance(self, nums: List[int]) -> int:
        """
        Record how many times each element occurs, then go over that dict to find
        the one which only occurs once
        """
        result = {}
        for each in nums:
            occurance = result.setdefault(each, 0) + 1
            result[each] = occurance
        
        for each in result:
            if result[each] == 1:
                return each
        return -1
