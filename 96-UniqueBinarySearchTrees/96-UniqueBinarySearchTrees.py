# Last updated: 23.09.2025, 10:14:02
class Solution:
    def numTrees(self, n: int) -> int:
        
        dp = [0] * (n+1)
        dp[0], dp[1] = 1, 1

        for node in range(2, n+1):
            for root in range(1, node+1):
                dp[node] += dp[root-1] * dp[node-root]
        
        return dp[n]
