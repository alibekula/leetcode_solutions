# Last updated: 26.01.2026, 03:42:39
1class Solution:
2    def findJudge(self, n: int, trust: List[List[int]]) -> int:
3
4        candidate = -1
5        graph = {i: set() for i in range(1, n+1)}
6
7        for u, v in trust:
8            graph[u].add(v)
9
10        for node in graph:
11            if not graph[node]:
12                if candidate != -1:
13                    return -1
14                else:
15                    candidate = node
16
17        for node in graph:
18            if node != candidate and candidate not in graph[node]:
19                return -1
20        
21        return candidate
22