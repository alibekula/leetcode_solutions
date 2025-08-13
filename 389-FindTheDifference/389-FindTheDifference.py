# Last updated: 13.08.2025, 16:57:34
class Solution:
    from collections import Counter
    def findTheDifference(self, s: str, t: str) -> str:
        counter1 = Counter(s)
        counter2 = Counter(t)
        diff = counter2 - counter1

        return ''.join(diff.keys())
        