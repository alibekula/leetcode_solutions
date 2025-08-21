# Last updated: 21.08.2025, 06:22:10
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        if not s:
            return 0
        
        n = len(s)
        max_length = 1
        dp = [[0 for _ in range(n)] for _ in range(n)]

        for i in range(n):
            dp[i][i] = 1
            for j in range(i-1, -1, -1):
                if s[i] == s[j]:
                    dp[j][i] = dp[j+1][i-1] + 2
                else:
                    dp[j][i] = max(dp[j+1][i], dp[j][i-1])

                max_length = max(max_length, dp[j][i])

        return max_length