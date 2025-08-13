# Last updated: 13.08.2025, 16:57:45
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s[:] = reversed(s)
