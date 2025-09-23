# Last updated: 23.09.2025, 16:40:43
class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        
        keys = set(brokenLetters)
        total = 0
        i = 0


        while i < len(text):
            
            broken = False

            while i < len(text) and text[i] != ' ':
                if text[i] in keys:
                    broken = True
                i += 1

            if not broken:
                total += 1
            
            i += 1

        return total