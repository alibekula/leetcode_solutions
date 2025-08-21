# Last updated: 21.08.2025, 10:12:19
from collections import Counter
class Solution:
    def partition(self, s: str) -> list[[str]]:
        
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]

        for i in range(n):
            dp[i][i] = True
            for j in range(i-1, -1, -1):
                if s[i] == s[j] and (i-j < 2 or dp[i-1][j+1]):
                    dp[i][j] = True

        ans = []
        curr = []

        def dfs(i):
            nonlocal n, s
            if i >= n:
                ans.append(curr[:])
                return

            for j in range(i, n):
                if dp[j][i]:
                    curr.append(s[i:j+1])
                    dfs(j+1)           
                    curr.pop() 

        dfs(0)
        return ans