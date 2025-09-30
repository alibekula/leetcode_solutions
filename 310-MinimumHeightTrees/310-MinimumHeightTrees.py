# Last updated: 30.09.2025, 09:13:02
from collections import defaultdict, deque
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        if n ==1:
            return [0]
        
        graph = defaultdict(set)
        degree = defaultdict(int)

        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

            degree[u] += 1
            degree[v] += 1
        
        candidates = deque([i for i in degree if degree[i] == 1])
        node_count = n

        while node_count > 2:
            width = len(candidates)
            node_count -= width

            for _ in range(width):
                node = candidates.popleft()
                for nei in graph[node]:
                    degree[nei] -= 1
                    if degree[nei] == 1:
                        candidates.append(nei)
        
        return list(candidates)
