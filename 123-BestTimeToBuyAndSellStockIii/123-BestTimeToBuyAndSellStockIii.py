# Last updated: 13.08.2025, 16:59:34
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)
        left = [0 for _ in range(len(prices))]
        right = [0 for _ in range(len(prices))]

        min_price = float('inf')
        max_profit = 0

        for i in range(n):
            min_price = min(min_price, prices[i])
            max_profit = max(max_profit, prices[i] - min_price)
            left[i] = max_profit
        
        max_price = float('-inf')
        max_profit = 0

        for j in range(n-1, -1, -1):
            max_price = max(max_price, prices[j])
            max_profit = max(max_price - prices[j], max_profit)
            right[j] = max_profit
        
        profit = 0

        for p in range(n):
            profit = max(left[p] + right[p], profit)
        
        return profit
