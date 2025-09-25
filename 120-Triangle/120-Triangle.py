# Last updated: 25.09.2025, 13:50:42
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = triangle[-1][:]
        n = len(dp)

        for level in range(n-2, -1, -1):
            for idx in range(len(triangle[level])):
                dp[idx] = triangle[level][idx] + min(dp[idx], dp[idx+1])
        
        return dp[0]