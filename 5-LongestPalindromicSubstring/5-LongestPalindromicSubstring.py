# Last updated: 21.08.2025, 07:06:54
class Solution:
    def expand_from_center(self, i, j):

        l, r = i, j

        while (r < self.n and l >= 0) and (self.s[l] == self.s[r]):
            l -= 1
            r += 1
        
        return [l+1, r-1]

    def longestPalindrome(self, s: str) -> str:
        self.n = len(s)
        self.s = s
        max_len = [0, 0]
        
        for i in range(self.n):

            odd = self.expand_from_center(i, i)
            even = self.expand_from_center(i, i+1)

            max_len = max(odd, even, max_len, key=lambda x: x[1] - x[0])
        
        return s[max_len[0]:max_len[1]+1]

