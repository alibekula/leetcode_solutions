# Last updated: 16.12.2025, 01:15:55
1class Solution:
2    def distributeCandies(self, candyType: List[int]) -> int:
3        n = len(candyType)
4        m = len(set(candyType))
5
6        return min(n//2, m)