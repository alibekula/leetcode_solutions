# Last updated: 29.01.2026, 13:43:38
1class Solution:
2    def minCost(self, grid: List[List[int]], k: int) -> int:
3        n, m = len(grid), len(grid[0])
4        
5        cells = []
6        for i in range(n):
7            for j in range(m):
8                cells.append((grid[i][j], i, j))
9        
10        cells.sort(key=lambda x: x[0], reverse=True)
11        
12        dp = [[float('inf')] * m for _ in range(n)]
13        dp[0][0] = 0
14        
15        def move():
16            for i in range(n):
17                for j in range(m):
18                    if dp[i][j] == float('inf'): continue
19                    
20                    if i + 1 < n:
21                        dp[i+1][j] = min(dp[i+1][j], dp[i][j] + grid[i+1][j])
22                    if j + 1 < m:
23                        dp[i][j+1] = min(dp[i][j+1], dp[i][j] + grid[i][j+1])
24        
25        move()
26        
27        for _ in range(k):
28            prev = [row[:] for row in dp]
29            min_val = float('inf')
30            
31            idx = 0
32            while idx < len(cells):
33                end = idx
34                curr_v = cells[idx][0]
35                
36                while end < len(cells) and cells[end][0] == curr_v:
37                    end += 1
38                
39                group_min = float('inf')
40                for k_i in range(idx, end):
41                    r, c = cells[k_i][1], cells[k_i][2]
42                    if prev[r][c] < group_min:
43                        group_min = prev[r][c]
44                
45                best = min(min_val, group_min)
46                
47                for k_i in range(idx, end):
48                    r, c = cells[k_i][1], cells[k_i][2]
49                    if best < dp[r][c]:
50                        dp[r][c] = best
51                
52                min_val = best
53                idx = end
54            
55            move()
56            
57        return dp[n-1][m-1]