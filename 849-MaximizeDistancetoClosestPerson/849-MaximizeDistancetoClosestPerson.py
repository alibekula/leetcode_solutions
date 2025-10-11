# Last updated: 11.10.2025, 20:15:13
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        
        n = len(seats)
        r = 1
        length = 1
        # 0 0 0 0 1
        # 1 0 0 0 0
        # 1 0 0 0 1
        # 0 0 1 0 0 1 0 0 0 0 0 0 

        while r < n:
            l = r - 1

            while r < n and seats[r] != 1:
                r += 1

            if r < n and seats[r] == 1 and seats[l] == 1:
                length = max(length, (r - l) // 2)
            else:
                new_length = r - l if seats[l] == 0 else r - l -1
                length = max(length, new_length)
            r += 1

        return length