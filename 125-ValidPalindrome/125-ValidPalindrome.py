# Last updated: 13.08.2025, 16:59:33
class Solution:
    def isPalindrome(self, s: str) -> bool:
        sett = set('qwertyuiopasdfghjklzxcvbnm1234567890')
        l, r = 0, len(s)-1

        while l <= r:
            while l <= r and s[l].lower() not in sett:
                l += 1
            
            while l <= r and s[r].lower() not in sett:
                r -= 1
            
            if  l <= r and s[l].lower() != s[r].lower():
                return False
            
            r -= 1
            l += 1
        
        return True
        