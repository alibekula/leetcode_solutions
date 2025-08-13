# Last updated: 13.08.2025, 16:59:37
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if not prices:
            return 0

        if len(prices) == 1:
            return 0

        profit = 0
        l, r = 0, 0
        min_price = prices[l]

        while r < len(prices):
            profit = max(profit, prices[r] - min_price)
            
            if prices[l] < min_price:
                min_price = prices[l]

            r += 1
            l += 1
        
        return profit
            



        