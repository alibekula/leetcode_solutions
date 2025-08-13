# Last updated: 13.08.2025, 16:58:47
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        dct_s = dict()
        dct_t = dict()

        for char_s, char_t in zip(s, t):

            if char_s not in dct_s:
                dct_s[char_s] = char_t
            else:
                if dct_s[char_s] != char_t:
                    return False
            
            if char_t not in dct_t:
                dct_t[char_t] = char_s
            else:
                if dct_t[char_t] != char_s:
                    return False
        
        return True
        