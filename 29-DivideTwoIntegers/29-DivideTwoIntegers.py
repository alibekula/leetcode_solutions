# Last updated: 13.08.2025, 17:01:05
from math import ceil

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
            
        minus = -1 if (dividend < 0) != (divisor < 0) else 1
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        if dividend == 0:
            return 0
        if divisor == 1:
            return dividend * minus
        if divisor > dividend:
            return 0
        ans = 0
        residual = dividend

        while residual >= divisor:
            tmp = divisor
            multiple = 1
            while (tmp<<1) <= residual:
                multiple <<= 1
                tmp <<= 1

            ans += multiple
            residual -= tmp
        return ans * minus 


