# Last updated: 28.01.2026, 03:58:22
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
19        visited = set()
20
21        while heap:
22            score, node = heapq.heappop(heap)
23
24            if node == n-1:
25                return score
26            
27            if node not in graph:
28                continue
29
30            visited.add(node)
31
32            for nei, wei in graph[node]:
33                if nei in visited:
34                    continue
35                
36                if min_dist[nei] > score + wei:
37                    heapq.heappush(heap, [score+wei, nei])
38                    min_dist[nei] = score + wei
39        
40        return -1