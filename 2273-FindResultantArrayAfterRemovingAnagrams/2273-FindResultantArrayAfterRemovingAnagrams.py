# Last updated: 13.10.2025, 07:33:51
from collections import Counter
class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        
        stack = []

        for word in words:
            counter = Counter(word)
            if not stack or stack[-1][1] != counter:
                stack.append([word, counter])
        
        return [word for word, _ in stack]