# Last updated: 31.01.2026, 11:48:04
1class Solution:
2    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
3        
4        for char in letters:
5            if char > target:
6                return char
7        
8        return letters[0]