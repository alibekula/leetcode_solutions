# Last updated: 13.08.2025, 16:58:05
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        if n ==1 :
            return 1
        l = 1
        r = n 
        while l < r:
            mid = (r-l)//2 + l
            if isBadVersion(mid):
                r = mid
            else:
                l =mid + 1
        return l
        