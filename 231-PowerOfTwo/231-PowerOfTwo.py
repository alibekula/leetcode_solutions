# Last updated: 13.08.2025, 16:58:22
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        if n == 0 or n < 0:
            return False

        sum_bits = 0

        for i in range(32):
            if (n>>i)&1:
                sum_bits += 1
            
            if sum_bits > 1:
                return False
        
        return True