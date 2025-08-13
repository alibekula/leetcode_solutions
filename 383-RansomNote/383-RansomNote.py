# Last updated: 13.08.2025, 16:57:37
from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter

        c1 = Counter(ransomNote)
        c2 = Counter(magazine)

        result = all(c1[char] <= c2[char] for char in c1)
        return result
        