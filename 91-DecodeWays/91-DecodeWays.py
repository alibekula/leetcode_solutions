# Last updated: 16.09.2025, 03:17:05
class Solution:
    def numDecodings(self, s: str) -> int:
        
        n = len(s)
        dp = [0] * (n+1)
        dp[0] = 1
        # 12
        # 0 1 
        for i in range(n):

            if s[i] =='0' and (i ==0 or s[i-1] not in ('1', '2')):
                return 0

            if i > 0 and ((s[i-1] == '1' and s[i] in '987654321') or (s[i-1] == '2' and s[i] in '123456')) and (i +1 >= n or s[i+1] != '0'):
                dp[i+1] = dp[i] + dp[i-1]
            else:
                dp[i+1] = dp[i]

        return dp[n]   