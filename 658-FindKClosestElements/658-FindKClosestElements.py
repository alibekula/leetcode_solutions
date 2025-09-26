# Last updated: 27.09.2025, 03:44:33
class Solution:
    def validPalindrome(self, s: str, k = 1, l=None, r = None) -> bool:
        
        if l is None or r is None:
            l, r = 0, len(s)-1

        while l <= r:
            if s[l] != s[r]:
                if k >= 1:
                    return self.validPalindrome(s, 0, l+1, r) or self.validPalindrome(s, 0, l, r-1)
                return False
            else:
                l += 1
                r -= 1
        
        return True