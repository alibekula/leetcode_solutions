# Last updated: 13.08.2025, 16:59:14
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        max_points = 0

        if n <= 2:
            return n
            
        for i in range(n):
            slopes = {}
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2,y2 = points[j]

                if x1 == x2:
                    slope = float('inf')
                else:
                    slope = (y1-y2)/(x1-x2)
                
                slopes[slope] = slopes.get(slope, 0) + 1

            for val in slopes.values():
                max_points = max(val+1, max_points)
        
        return max_points

            