# Last updated: 12.09.2025, 06:20:39
from math import ceil
class Solution:

    def get_min_hours(self, k):
        count = 0

        for pile in self.piles:
            count += ceil(pile / k)
        return count
    
    def search(self, l, r, h):

        ans = r
        while l <= r:
            mid = (l+r)//2
            hours = self.get_min_hours(mid)

            if hours <= h:
                r = mid - 1
                ans = min(mid, ans)
            else:
                l = mid + 1
        
        return ans


    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        if not piles:
            return 0
        
        n = len(piles)
        self.piles = piles

        if n > h:
            return -1
        
        max_count = max(piles)
        return self.search(1, max_count, h)

