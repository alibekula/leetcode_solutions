# Last updated: 13.08.2025, 16:57:51
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True
            
        if n == 0:
            return False

        if n < 0:
            return False

        curr = 3

        while curr < n:
            curr *= 3
        
        return curr == n
