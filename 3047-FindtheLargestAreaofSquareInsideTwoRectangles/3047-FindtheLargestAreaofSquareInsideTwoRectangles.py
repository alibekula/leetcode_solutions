# Last updated: 21.01.2026, 08:29:01
1class Solution:
2    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
3        max_side = 0
4        n = len(bottomLeft)
5
6        for i in range(n):
7            x, y = bottomLeft[i] 
8            x1, y1 = topRight[i]
9            for j in range(i+1, n):
10                p, q = bottomLeft[j]
11                p1, q1 = topRight[j]
12                
13                a = max(p, x)
14                b = max(y, q)
15                c = min(x1, p1)
16                d = min(y1, q1)
17
18                max_side = max(max_side, min(c-a, d-b))
19
20        return max_side**2