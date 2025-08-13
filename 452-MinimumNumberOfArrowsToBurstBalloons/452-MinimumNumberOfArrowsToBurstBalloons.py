# Last updated: 13.08.2025, 16:57:24
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:

        if not points:
            return 0
        
        if len(points) == 1:
            return 1

        points.sort(key = lambda x: x[0])
        ans = [points[0]]

        for start, finish in points:
            if ans[-1][1] >= start:
                ans[-1] = [start, min(finish, ans[-1][1])]
            else:
                ans.append([start, finish])

        return len(ans) 


        