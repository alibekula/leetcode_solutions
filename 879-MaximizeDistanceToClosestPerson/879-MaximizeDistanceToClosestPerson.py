# Last updated: 13.08.2025, 16:56:51
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        l, r = 0, 0
        longest = 0
        # 1
        # 1 0 0 0 0 1 |
        # 0 0 0 0 0 1
        # 1 0 0 0 0 0

        while r < len(seats):
            
            while r + 1< len(seats) and seats[r] == 0:
                r += 1
            
            if seats[r] == 1 and seats[l] == 1:
                longest = max(longest, (r - l)//2 )
            else:
                longest = max(longest, r-l)

            l = r
            r += 1
        
        return longest
        