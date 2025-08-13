# Last updated: 13.08.2025, 16:58:10
class Solution:
    def isUgly(self, n: int) -> bool:

        if n == 0:
            return False

        while n % 2 == 0:
            n //= 2
        
        if n == 1:
            return True
        
        while n % 3 == 0:
            n //= 3
        
        if n == 1:
            return True
        
        while n%5 == 0:
            n //= 5
        
        if n == 1:
            return True
        
        return False