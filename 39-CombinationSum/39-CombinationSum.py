# Last updated: 19.08.2025, 03:50:44
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        l, r = 0, n-1

        while l <= r:
            mid = (l+r)//2

            if not isBadVersion(mid):
                l = mid + 1
            else:
                r = mid - 1
        
        return r + 1