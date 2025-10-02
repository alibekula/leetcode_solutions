# Last updated: 02.10.2025, 08:27:09
class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        
        full = numBottles
        empty = 0 
        count = 0

        while full > 0:
            count += full
            empty += full
            full = 0

            while empty >= numExchange:
                full += 1
                empty -= numExchange
                numExchange += 1
        
        return count
