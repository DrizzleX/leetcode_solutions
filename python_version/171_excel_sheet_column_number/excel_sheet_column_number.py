#!/bin/env python
class Solution:
    def letter_to_number(self, letter):
        """
        >>> solution = Solution()
        >>> solution.letter_to_number('A')
        1
        >>> solution.letter_to_number('b')
        2
        >>> solution.letter_to_number('Z')
        26
        """
        return ord(letter.upper()) - ord('A') + 1

    def titleToNumber(self, s: str) -> int:
        result = 0
        for each in s:
            result *= 26
            result += self.letter_to_number(each)
        return result
        
