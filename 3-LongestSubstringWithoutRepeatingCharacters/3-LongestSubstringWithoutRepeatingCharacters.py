# Last updated: 27.09.2025, 05:08:58
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        longest = 0
        n = len(s)
        l, r = 0, 0
        sett = set()

        while r < n:
            while r < n and s[r] not in sett:
                sett.add(s[r])
                longest = max(longest, len(sett))
                r += 1
            
            while r < n and s[r] in sett:
                sett.discard(s[l])
                l += 1

        return longest


        
