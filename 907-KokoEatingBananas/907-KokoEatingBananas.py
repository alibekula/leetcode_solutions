# Last updated: 13.08.2025, 16:56:49
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_count = 0
        for i in piles:
            if i > max_count:
                max_count = i
        l = 1
        r = max_count
        count = 0
        while l <= r:
            mid = (r+l)//2

            for i in piles:
                count += (i+mid-1)//mid

            if count <= h:
                r = mid - 1
            else:
                l = mid + 1
            count = 0
        return l
        