# Last updated: 13.08.2025, 16:57:30
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0] * 26
        n = len(s)
        longest = 0
        l = 0

        for r, char in enumerate(s):
            count[ord(char) - ord('A')] += 1

            while (r - l + 1) - max(count) > k:
                count[ord(s[l]) - ord('A')] -= 1
                l += 1
            
            longest = max(longest, r - l + 1)
        
        return longest



