# Last updated: 25.01.2026, 03:33:32
1class Solution:
2    def maximumAmount(self, coins: List[List[int]]) -> int:
3        
4        n, m = len(coins), len(coins[0])
5        dp = [[[float('-inf') for _ in range(3)] for _ in range(m+1)] for _ in range(n+1)]
6
7        for i in range(n-1, -1, -1):
8            for j in range(m-1, -1, -1):
9                val = coins[i][j]
10
11                for k in range(3):
12
13                    if i == n-1 and j == m-1:
14                        if val < 0 and k > 0:
15                            dp[i][j][k] = 0
16                        else:
17                            dp[i][j][k] = val
18                    
19                    else:
20
21                        right = dp[i+1][j][k] 
22                        down = dp[i][j+1][k]
23                        max_prev = max(right, down)
24                        res_neg = float('-inf')
25
26                        if val < 0 and k > 0:
27                                res_neg = max(dp[i+1][j][k-1], dp[i][j+1][k-1])
28                        res_pos = val + max_prev
29                        
30                        dp[i][j][k] = max(res_pos, res_neg)
31            
32        return dp[0][0][2]
33