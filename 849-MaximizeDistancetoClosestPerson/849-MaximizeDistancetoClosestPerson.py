# Last updated: 11.10.2025, 20:53:16
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        
        n = len(seats)
        length = 1
        # 0 0 0 0 1
        # 1 0 0 0 0
        # 1 0 0 0 1
        # 0 0 1 0 0 1 0 0 0 0 0 0 

        used = (i for i, seat in enumerate(seats) if seat == 1)
        prev = None
        future = next(used, None)

        for idx, seat in enumerate(seats):
            if seat:
                prev = idx
            else:

                while future is not None and future < idx:
                    future = next(used, None)

                left = float('inf') if prev is None else idx - prev
                right = float('inf') if future is None else future - idx

                length = max(length, min(left, right))
        
        return length