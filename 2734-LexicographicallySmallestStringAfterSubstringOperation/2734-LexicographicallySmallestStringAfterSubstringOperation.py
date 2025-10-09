# Last updated: 09.10.2025, 19:46:36
class Solution:
    def smallestString(self, s: str) -> str:

        if not s:
            return ''
        
        chars = list(s)
        n = len(chars)
        l= n-1

        for i in range(n):
            if chars[i] != 'a':
                l = i
                break
        
        if l == n-1:
            
            if chars[-1] == 'a':
                chars[-1] = 'z'
            else:
                chars[-1] = chr(ord(chars[-1]) - 1)
            
            return ''.join(chars)   
        
        r = l
        
        for j in range(l+1, n):
            if chars[j] != 'a':
                r = j
            else:
                break
        
        for k in range(l, r+1):
            chars[k] = chr(ord(chars[k]) -1)
        
        return ''.join(chars)

