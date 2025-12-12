# Last updated: 12.12.2025, 13:01:28
1class Solution:
2    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
3
4        n, m = len(grid), len(grid[0])
5        X = [0] * m
6        Y = [0] * m
7        ans = 0
8
9        for i in range(n):
10            row_x = 0
11            row_y = 0
12            for j in range(m):
13                row_x += grid[i][j] == 'X'
14                row_y += grid[i][j] == 'Y'
15
16                X[j] += row_x
17                Y[j] += row_y
18
19                ans += (X[j] > 0) & (X[j] == Y[j])
20            
21        return ans
22
23
24