# Last updated: 11.10.2025, 22:46:31
from collections import deque

class Solution:
    def coinChange(self, coins, amount):
        if amount == 0:
            return 0
        
        coins.sort()
        dp = {c: 1 for c in coins}
        queue = deque(coins)
        
        if min(coins) > amount:
            return -1
        if amount in dp:
            return 1

        while queue:
            curr = queue.popleft()
            for coin in coins:
                new_amount = curr + coin
                if new_amount > amount:
                    break
                if new_amount not in dp:
                    dp[new_amount] = dp[curr] + 1
                    if new_amount == amount:
                        return dp[new_amount]
                    queue.append(new_amount)
        return -1
