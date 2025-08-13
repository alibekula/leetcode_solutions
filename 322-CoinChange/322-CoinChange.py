# Last updated: 13.08.2025, 16:57:50
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')]*(amount+1)
        dp[0] = 0
        for coin in coins:
            for k in range(coin, amount+1):
                dp[k] = min(dp[k], dp[k-coin]+1)
        print(dp)
        return dp[amount] if dp[amount] != float('inf') else -1

