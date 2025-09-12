# Last updated: 12.09.2025, 16:19:23
class Solution:
    def doesAliceWin(self, s: str) -> bool:
        
        vowels = set('aeiou')
        count = 0
        last_vowel_idx = None
        for idx, char in enumerate(s):
            if char in vowels:
                count += 1
                last_vowel_idx = idx
        
        if count == 0:
            return False
        return True

        
