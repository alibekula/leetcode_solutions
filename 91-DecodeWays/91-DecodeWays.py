# Last updated: 17.08.2025, 20:35:55
class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s):1}

        def search(curr):
            if curr in dp:
                return dp[curr]
            if curr >= len(s):
                return 
            if s[curr] == '0':
                return 0

            res = search(curr+1)

            if curr+1 < len(s) and ((s[curr] in '2' and s[curr+1] in '0123456') or (s[curr] == '1')):
                res += search(curr+2)
            
            dp[curr] = res

            return res
        
        return search(0)