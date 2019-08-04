#!/bin/env python
from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = defaultdict(int)
        for each in s:
            count[each] += 1
        for each in t:
            count[each] -= 1
        for cnt in count.values():
            if cnt != 0:
                return False
        return True

    def isAnagram_sort(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
        