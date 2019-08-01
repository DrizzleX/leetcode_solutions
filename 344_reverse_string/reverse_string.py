from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s_len = len(s)
        for i in range(s_len//2):
            s[i], s[s_len-1-i] = s[s_len-1-i], s[i]