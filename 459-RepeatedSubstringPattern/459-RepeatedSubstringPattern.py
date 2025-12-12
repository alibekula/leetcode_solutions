# Last updated: 12.12.2025, 19:00:14
1class Solution:
2    def repeatedSubstringPattern(self, s: str) -> bool:
3        
4        return s in (s*2)[1:len(s*2)-1]