# Last updated: 13.08.2025, 16:57:33
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l, r = 0, 0

        while l < len(s) and r < len(t):
            if s[l] == t[r]:
                l += 1
                r += 1
            else:
                r += 1
        
        return len(s) ==  l

        