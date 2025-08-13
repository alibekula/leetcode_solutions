# Last updated: 13.08.2025, 16:57:03
class Solution:
    def validPalindrome(self, s: str, l= 0, r = None, flag=True) -> bool:

        r = len(s)-1 if r is None else r 

        while l <= r:

            if s[l] != s[r]:
                if flag:
                    return self.validPalindrome(s, l+1, r, flag=False) or self.validPalindrome(s, l, r-1, flag=False)
                else:
                    return False
            
            l += 1
            r -= 1
        
        return True
        