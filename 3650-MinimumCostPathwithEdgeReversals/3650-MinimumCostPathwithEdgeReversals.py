# Last updated: 28.01.2026, 05:03:25
1class Solution:
2    def minCost(self, n: int, edges: List[List[int]]) -> int:
3        
4        graph = {}
5        min_dist = {i: float('inf') for i in range(n)}
6
7        for u, v, w in edges:
8            if u not in graph:
9                graph[u] = []
10
11            graph[u].append([v, w])
12
13            if v not in graph:
14                graph[v] = []
15            
16            graph[v].append([u, w*2])
17        
18        heap = [[0, 0]]
19
20        while heap:
21            score, node = heapq.heappop(heap)
22
23            if node == n-1:
24                return score
25            
26            if node not in graph:
27                continue
28            
29            if min_dist[node] < score:
30                continue
31
32
33            for nei, wei in graph[node]:
34                if min_dist[nei] > score + wei:
35                    heapq.heappush(heap, [score+wei, nei])
36                    min_dist[nei] = score + wei
37        
38        return -1