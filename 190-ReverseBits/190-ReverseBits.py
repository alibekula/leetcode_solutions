# Last updated: 13.08.2025, 16:58:57
class Solution:
    def reverseBits(self, n: int) -> int:
        
        res = 0

        for _ in range(32):

            res = (res << 1) | (n & 1)
            n >>= 1
        
        return res