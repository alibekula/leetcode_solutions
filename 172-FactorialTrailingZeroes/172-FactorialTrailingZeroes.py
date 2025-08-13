# Last updated: 13.08.2025, 16:59:03
class Solution:
    def trailingZeroes(self, n: int) -> int:
        
        power_of_5 = 5
        count = 0

        while power_of_5 <= n:
            count += n // power_of_5
            power_of_5 *= 5
        
        return count