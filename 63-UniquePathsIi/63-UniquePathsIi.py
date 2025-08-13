# Last updated: 13.08.2025, 17:00:31
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n, m = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for _ in range(m)] for _ in range(n)]
        dp[0][0] = 1 if obstacleGrid[0][0] != 1 else 0

        for i in range(n):
            for j in range(m):

                if obstacleGrid[i][j] == 1:
                    continue

                if i-1 < 0:
                    top = 0
                else:
                    top = dp[i-1][j]
                
                if j-1 < 0:
                    left = 0
                else:
                    left = dp[i][j-1]
                
                dp[i][j] = dp[i][j] + top + left
        
        return dp[-1][-1]