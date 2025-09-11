# Last updated: 11.09.2025, 07:15:55
class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = set('aeiouAEIOU')
        order = "AEIOUaeiou"  
        freq = {ch: 0 for ch in order}
        
        lst = list(s)
        
        for ch in s:
            if ch in vowels:
                freq[ch] += 1
        
        idx = 0  
        for i, ch in enumerate(lst):
            if ch in vowels:
                while idx < len(order) and freq[order[idx]] == 0:
                    idx += 1
                lst[i] = order[idx]
                freq[order[idx]] -= 1
        
        return ''.join(lst)
