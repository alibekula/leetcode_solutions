# Last updated: 13.08.2025, 16:56:31
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0
        freq = {'a': 0, 'b': 0, 'c': 0}
        l = 0
        
        # Expand the window with r.
        for r in range(n):
            freq[s[r]] += 1
            
            # While the current window [l, r] is valid (all characters seen),
            # move l to shrink the window from the left.
            while freq['a'] > 0 and freq['b'] > 0 and freq['c'] > 0:
                freq[s[l]] -= 1
                l += 1
            
            # All substrings ending at r that start in the range [0, l-1] are valid.
            count += l
        
        return count
