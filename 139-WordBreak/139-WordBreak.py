# Last updated: 13.08.2025, 16:59:20
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        sett = set(wordDict)
        dp = [False for _ in range(len(s)+1)]
        dp[0] = True

        for i in range(1, len(s)+1):
            for j in range(i):
                if dp[j] and s[j:i] in sett:
                    dp[i] = True
                    break
        
        return dp[-1]