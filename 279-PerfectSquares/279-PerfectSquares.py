# Last updated: 13.08.2025, 16:58:04
class Solution:
    def numSquares(self, n: int) -> int:

        if int(n**0.5)**2 == n:
            return 1

        for a in range(int(n ** 0.5)+1):
            b = n - a ** 2

            if int(b**0.5)**2 + a ** 2 == n:
                return 2
        
        # n = 4^m * (8k - 7)

        tmp = n

        while tmp % 4 == 0:
            tmp //= 4
        
        if tmp%8 == 7:
            return 4
        
        return 3

        