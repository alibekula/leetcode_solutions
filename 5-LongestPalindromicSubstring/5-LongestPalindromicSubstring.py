# Last updated: 21.08.2025, 06:59:56
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        if n == 0:
            return ''

        dp = [[False for _ in range(n)] for _ in range(n)]
        max_str = s[0]

        for i in range(n):
            dp[i][i] = True

            for j in range(i-1, -1, -1):
                if s[i] == s[j] and (dp[j+1][i-1] or i-j < 2):
                    dp[j][i] = True

                    if i - j + 1 > len(max_str):
                        max_str = s[j: i+1]
            
        return max_str