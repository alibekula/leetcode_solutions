# Last updated: 13.08.2025, 16:57:41
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num in (1, 0):
            return num
        l = 1
        r = num // 2
        while l<=r:
            mid = (r-l)//2 + l
            if mid * mid == num:
                return True
            elif mid*mid > num:
                r = mid - 1
            else:
                l = mid +1
        return False
