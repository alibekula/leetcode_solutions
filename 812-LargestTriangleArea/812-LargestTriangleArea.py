# Last updated: 27.09.2025, 07:24:40
class Solution:
    def calc_dist(self, x1, y1, x2, y2):
        return abs(x1 - x2) + abs(y1 - y2)
    
    def calc_area(self, x1, x2, x3, y1, y2, y3):
        return (1/2) * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))

    def largestTriangleArea(self, points: List[List[int]]) -> float:
        
        edges = set()
        n = len(points)
        
        for i in range(n-1):
            for j in range(i+1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                edges.add((x1, y1, x2, y2))
        
        max_area = 0

        for edge in edges:
            x1, y1, x2, y2 = edge

            for a, b in points:
                candidate1 = (x1, y1, a, b)
                candidate2 = (a, b, x1, y1)
                candidate3 = (x2, y2, a, b)
                candidate4 = (a, b, x2, y2)

                if (candidate1 in edges or candidate2 in edges) and (candidate3 in edges or candidate4 in edges):
                    max_area = max(max_area, self.calc_area(x1, x2, a, y1, y2, b))
        
        return max_area
        