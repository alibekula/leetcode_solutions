# Last updated: 13.08.2025, 17:00:32
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 if i != 0 else 1 for i in range(n)] if j != 0 else [1 for k in range(n)] for j in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]
        