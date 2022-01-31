#!/bin/env python
from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        This is the fastest in Python 3
        """
        if len(s)!= len(t):
            return False
        c = set(s)
        for i in c:
            if s.count(i) != t.count(i):
                return False
        return True

    def isAnagram_a_z_occurance(self, s: str, t: str) -> bool:
        s_occurance = [0 for i in range(26)]
        t_occurance = [0 for i in range(26)]
        a_ord = ord('a')
        for each in s:
            s_occurance[ord(each) - a_ord] += 1
        for each in t:
            t_occurance[ord(each) - a_ord] += 1

        for i in range(26):
            if s_occurance[i] != t_occurance[i]:
                return False
        return True

    def isAnagram_dict(self, s: str, t: str) -> bool:
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
        