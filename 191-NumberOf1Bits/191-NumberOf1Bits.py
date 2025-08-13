# Last updated: 13.08.2025, 16:58:55
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0 

        for _ in range(32):
            count += n&1
            n >>= 1
        
        return count