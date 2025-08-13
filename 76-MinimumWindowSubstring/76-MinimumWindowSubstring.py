# Last updated: 13.08.2025, 17:00:16
from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        # Edge cases
        if not s or not t:
            return ""

        counter = Counter(t)      # frequencies of chars in t
        window = {}               # frequencies of those chars in current window
        size = len(counter)       # number of distinct characters that need matching
        formed = 0                # how many distinct chars are currently "fully matched"
        l = 0                     # window start
        shortest = (float('inf'), "")  # (window_length, substring)

        # Expand window [l..r]
        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1

            # If s[r] is a needed character and we've reached the needed freq
            if s[r] in counter and window[s[r]] == counter[s[r]]:
                formed += 1

            # Try to shrink from the left as long as we have a valid window
            while l <= r and formed == size:
                current_len = r - l + 1
                # If this window is smaller, update our record
                if current_len < shortest[0]:
                    shortest = (current_len, s[l:r+1])

                # Pop from the left
                window[s[l]] -= 1
                # If dropping below the required freq, we're no longer fully matched
                if s[l] in counter and window[s[l]] < counter[s[l]]:
                    formed -= 1
                l += 1

        return shortest[1] if shortest[0] != float('inf') else ""
