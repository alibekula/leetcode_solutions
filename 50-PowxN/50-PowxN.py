# Last updated: 13.08.2025, 17:00:43
class Solution:
    
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        if n < 0:
            x = 1 / x
            n = -n

        ans = 1.0
        base = x

        while n > 0:
            if n % 2 == 1:  
                ans *= base
            base *= base  
            n //= 2

        return ans
