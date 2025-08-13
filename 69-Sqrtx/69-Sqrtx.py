# Last updated: 13.08.2025, 17:00:24
class Solution:
    def mySqrt(self, x: int, max_val = 46340) -> int:
        left, right = 0, max_val
        
        while left <= right:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1
        

        return right

