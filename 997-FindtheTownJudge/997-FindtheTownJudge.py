# Last updated: 26.01.2026, 03:48:40
1class Solution:
2    def findJudge(self, n: int, trust: List[List[int]]) -> int:
3
4        in_degree = {i: [0, 0] for i in range(1, n+1)}
5
6        for u, v in trust:
7            in_degree[u][0] += 1
8            in_degree[v][1] += 1
9        
10        for node in in_degree:
11            i, j = in_degree[node]
12
13            if i == 0 and j == n-1:
14                return node
15        
16        return -1
17