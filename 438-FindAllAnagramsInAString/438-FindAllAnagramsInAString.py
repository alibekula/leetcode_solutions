# Last updated: 13.08.2025, 16:57:27
class Solution:
    from collections import Counter
    def findAnagrams(self, s: str, p: str) -> List[int]:
        counter = Counter(p)
        window = Counter(s[:len(p)])

        prev = 0
        ans = []

        if counter == window:
            ans.append(0)

        for char in s[len(p):]:
            window[s[prev]] -= 1

            if window[s[prev]] == 0:
                del window[s[prev]]

            prev += 1

            if char not in window:
                window[char] = 0

            window[char] += 1

            if window == counter:
                ans.append(prev)
        
        return ans 
