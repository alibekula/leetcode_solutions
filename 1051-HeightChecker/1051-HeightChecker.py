# Last updated: 22.01.2026, 00:25:12
1class Solution:
2    def heightChecker(self, heights: List[int]) -> int:
3        expected = sorted(heights)
4        total = 0
5
6        for a, b in zip(expected, heights):
7
8            if a != b:
9                total += 1
10
11        return total