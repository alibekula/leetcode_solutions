# Last updated: 13.08.2025, 16:56:33
from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # Create a counter for the characters in the text
        counter = Counter(text)
        
        # Divide counts of 'l' and 'o' by 2
        counter['l'] //= 2
        counter['o'] //= 2
        
        # Find the minimum count for the characters in 'balloon'
        min_val = min(counter[char] for char in 'balon')
        
        return min_val
