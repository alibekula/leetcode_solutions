# Last updated: 13.08.2025, 16:56:26
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        tmp = numBottles
        ans = tmp
        while tmp >= numExchange:
            ans += tmp // numExchange
            tmp = tmp // numExchange + tmp % numExchange
        return ans