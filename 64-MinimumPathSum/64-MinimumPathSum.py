# Last updated: 13.08.2025, 17:00:29
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        dp = [[float('inf') for _ in range(m)] for _ in range(n)]
        dp[0][0] = grid[0][0]

        for i in range(n):
            for j in range(m):

                if i - 1 >= 0:
                    left = dp[i-1][j]
                else:
                    left = float('inf')
                
                if j - 1 >= 0:
                    top = dp[i][j-1]
                else:
                    top = float('inf')
                
                dp[i][j] = grid[i][j] + min(left, top) if any([i != 0, j != 0]) else dp[i][j]

        return dp[-1][-1] 

        