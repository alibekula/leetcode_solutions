# Last updated: 11.12.2025, 16:36:56
1class Solution:
2    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
3        
4        bound_x = {}
5        bound_y = {}
6
7        for b in buildings:
8            x, y = b
9            min_y, max_y = bound_x.get(x, [float('inf'), float('-inf')])
10            min_x, max_x = bound_y.get(y, [float('inf'), float('-inf')])
11
12            min_y = min(y, min_y)
13            max_y = max(y, max_y)
14            min_x = min(x, min_x)
15            max_x = max(x, max_x)
16
17            bound_x[x] = [min_y, max_y]
18            bound_y[y] = [min_x, max_x]
19            
20        total = 0
21
22        for b in buildings:
23            x, y = b
24
25            min_y, max_y = bound_x[x]
26            min_x, max_x = bound_y[y]
27
28            if (min_x < x < max_x) and (min_y < y < max_y):
29                total += 1
30        
31        return total
32
33