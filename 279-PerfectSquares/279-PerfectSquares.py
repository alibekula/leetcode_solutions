# Last updated: 11.10.2025, 00:55:27
class Solution:
    def numSquares(self, n: int) -> int:
        
        if int(n**0.5) == n**0.5:
            return 1
        
        tmp = n
        for i in range(1, int(n**0.5)+1):
            a = i**2
            b = tmp - a
            if int(b**0.5) == b**0.5:
                return 2
        
        # a + b + c + d = n
        # 0 1 2 3 
        # i * 

        while n % 4 == 0:
            n //= 4

        if n % 8 == 7:
            return 4

        return 3