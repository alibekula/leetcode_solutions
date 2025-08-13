# Last updated: 13.08.2025, 16:59:38
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = triangle[-1][:]

        for level in range(len(triangle)-2,-1, -1):
            for idx in range(len(triangle[level])):
                dp[idx] = triangle[level][idx] + min(dp[idx], dp[idx+1])

        return dp[0] 