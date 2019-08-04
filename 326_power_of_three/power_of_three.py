#!/bin/env python
import re
def baseN(num, b, numerals="0123456789abcdefghijklmnopqrstuvwxyz"):
    return '-'+baseN(-num, b) if num < 0 else ((num == 0) and numerals[0]) or (baseN(num // b, b, numerals).lstrip(numerals[0]) + numerals[num % b])

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        """
        Convert base 10 number to base 3 and the representation will be:
        1 -> 1
        3 -> 10
        9 -> 100
        27 -> 1000

        Therefore, any number that is power of 3 will be a 1 followed by zero or more 0
        """
        return re.match('^10*$', baseN(n, 3)) is not None

    def isPowerOfThree_loop(self, n: int) -> bool:
        while n:
            if n == 1:
                return True
            if n % 3 == 0:
                n //= 3
            else:
                return False
        return False
        