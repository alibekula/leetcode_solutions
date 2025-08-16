# Last updated: 16.08.2025, 16:28:14
import heapq
class Solution:
    def _find(self, node):
        if self.roots[node] == node:
            return node
        
        self.roots[node] = self._find(self.roots[node])
        return self.roots[node]
    
    def _union(self, node1, node2):
        root1 = self._find(node1)
        root2 = self._find(node2)

        if root1 != root2:
            self.roots[root1] = root2
            return True
        
        return False

    def _calc_dist(self, point1, point2):
        x1, y1 = point1
        x2, y2 = point2

        return abs(x1-x2) + abs(y2-y1)

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        points = [tuple(point) for point in points]
        graph = {key: [] for key in points} 

        for i in range(n):
            x = points[i]
            for j in range(i+1, n):
                y = points[j]
                dist = self._calc_dist(x, y)
                graph[x].append([dist, y])
                graph[y].append([dist, x])
        
        visited = set()
        heap = []
        heapq.heappush(heap, [0, points[0]])
        sum_dist = 0

        while len(visited) < n:
            dist, point = heapq.heappop(heap)

            if point in visited:
                continue

            visited.add(point)
            sum_dist += dist

            for new_dist, adj in graph[point]:
                if adj not in visited:      
                    heapq.heappush(heap, [new_dist, adj])
        
        return sum_dist
        
