# Last updated: 21.08.2025, 02:58:52
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        if amount == 0:
            return 1
        
        coins.sort()
        dp = [0 for _ in range(amount + 1)]
        dp[0] = 1

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i-coin]
 

        return dp[amount]


                