# Last updated: 13.08.2025, 16:57:58
class Solution:
    from collections import defaultdict
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        s = s.split()

        if len(pattern) != len(s):
            return False

        dct1 = {}
        dct2 = {}

        for char, word in zip(pattern, s):
            if word in dct1:
                if dct1[word] != char:
                    return False

            else:
                dct1[word] = char

            if char in dct2:
                if dct2[char] != word:
                    return False
            
            else:
                dct2[char] = word
        
        return True