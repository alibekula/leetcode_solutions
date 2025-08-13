# Last updated: 13.08.2025, 16:59:35
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 0
        profit = 0
        curr_min = prices[l]

        while r < len(prices):

            if prices[r] >= prices[l]:
                profit += prices[r] - prices[l]
                l = r
            else:
                l += 1

            r += 1
        
        return profit
            

        