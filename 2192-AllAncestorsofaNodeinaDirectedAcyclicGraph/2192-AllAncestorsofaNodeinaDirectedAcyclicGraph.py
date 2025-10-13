# Last updated: 13.10.2025, 23:47:25
from collections import deque
class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        in_degree = {i: 0 for i in range(n)}
        graph = {j: [] for j in range(n)}

        for start, end in edges:
            in_degree[end] += 1
            graph[start].append(end)
        
        output = [set() for i in range(n)]
        queue = deque([j for j in in_degree if in_degree[j] == 0])
        seen = set()

        while queue:
            node = queue.popleft()
            seen.add(node)

            for nei in graph[node]:
                in_degree[nei] -= 1
                output[nei].update(output[node])
                output[nei].add(node)

                if in_degree[nei] == 0:
                    queue.append(nei)

                

        return [sorted(o) for o in output]

