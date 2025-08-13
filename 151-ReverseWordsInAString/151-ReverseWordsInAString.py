# Last updated: 13.08.2025, 16:59:12
class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(reversed(s.strip().split()))
        