# Last updated: 13.08.2025, 16:59:00
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        n, m = len(dungeon), len(dungeon[0])

        dp = [[float('inf') for _ in range(m+1)] for _ in range(n+1)]
        dp[n-1][m] = dp[n][m-1] = 1  
        
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                tmp = min( dp[i+1][j] - dungeon[i][j], dp[i][j+1] - dungeon[i][j])
                dp[i][j] = max(1, tmp)

        return max(1, dp[0][0])