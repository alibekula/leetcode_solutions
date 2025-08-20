# Last updated: 21.08.2025, 02:18:17
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
            self.roots[root2] = root1
            return False
        
        return True
    
    def _calc_dist(self, node1, node2):
        x1, y1 = node1
        x2, y2 = node2

        return abs(x1 - x2) + abs(y1 - y2)

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        points = [tuple(i) for i in points]
        visited = [False for _ in range(n)]
        k = n-1

        self.roots = {key: value for key, value in zip(points, points)}

        edges = []

        for i in range(n):
            p1 = points[i]
            for j in range(i+1, n):
                p2 = points[j]
                edges.append([self._calc_dist(p1, p2), p1, p2])
        
        edges.sort()
        ans = 0

        for edge in edges:
            dist, p1, p2 = edge

            if not self._union(p1, p2):
                ans += dist
                k -= 1
            
            if k == 0:
                return ans
        
        return ans

        

            

