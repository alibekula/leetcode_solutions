# Last updated: 01.10.2025, 10:12:18
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        
        if (numExchange == 1 and numBottles >= 1):
            return float('inf')

        count = 0
        full = numBottles
        empty = 0

        while full > 0:
            count += full
            empty = full + empty
            full = empty // numExchange
            empty -= full * numExchange


        return count