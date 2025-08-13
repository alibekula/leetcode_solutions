# Last updated: 13.08.2025, 16:58:30
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n, m = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(len(matrix[0])+1)] for _ in range(len(matrix)+1)]
        max_square = 0
        
        for i in range(1, n+1):
            for j in range(1, m+1):
                curr = int(matrix[i-1][j-1])
                dp[i][j] =  curr + min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) if curr else 0
                max_square = max(max_square, dp[i][j])
        
        return max_square**2
