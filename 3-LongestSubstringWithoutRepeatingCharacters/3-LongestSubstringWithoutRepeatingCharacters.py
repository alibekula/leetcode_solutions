# Last updated: 27.09.2025, 04:00:26
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r =0, 0
        sett = set()
        longest = 0

        while r < len(s):

            if s[r] in sett:

                while s[r] in sett:
                    sett.remove(s[l])
                    l += 1
            
            sett.add(s[r])
            longest = max(longest, r-l+1)
            r += 1
        
        return longest

