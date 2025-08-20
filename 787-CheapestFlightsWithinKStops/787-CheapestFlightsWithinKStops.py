# Last updated: 21.08.2025, 02:35:17
from collections import defaultdict

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        if not points:
            return 0

        n = len(points)
        points = [ tuple(i) for i in points]

        graph = defaultdict(list)

        for i in range(n):
            p1 = points[i]
            for j in range(i+1, n):
                p2 = points[j]
                dist = abs(p1[0] - p2[0]) + abs(p1[1]-p2[1])
                graph[p1].append([dist, p1, p2])
                graph[p2].append([dist, p2, p1])
            
        heap = [[0, points[0]]]
        visited = set()
        res = 0

        while len(visited) < n:
            dist, p = heapq.heappop(heap)

            if p in visited:
                continue

            visited.add(p)
            res += dist

            for node in graph[p]:
                new_dist, p1, p2 = node
                if p2 not in visited:
                    heapq.heappush(heap, [new_dist, p2])
        
        return res

