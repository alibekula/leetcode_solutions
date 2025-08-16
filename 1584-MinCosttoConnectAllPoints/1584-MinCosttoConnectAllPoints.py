# Last updated: 16.08.2025, 16:11:52
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
        self.roots = {key: value for key, value in zip(points, points)}

        edges = []

        for i in range(n):
            x = points[i]
            for j in range(i+1, n):
                y = points[j]
                dist = self._calc_dist(x, y)
                edges.append([dist, x, y])
        
        edges.sort(key=lambda x: x[0])
        sum_weight = 0
        num_nodes = 0

        for w, x, y in edges:
            if self._union(x, y):
                num_nodes += 1
                sum_weight += w

                if num_nodes == n-1:
                    return sum_weight

        return sum_weight