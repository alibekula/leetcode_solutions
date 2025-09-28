# Last updated: 28.09.2025, 10:16:10
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        if not intervals:
            return []
            
        intervals.sort(key=lambda x: x[0])

        n = len(intervals)
        ans = [intervals[0]]

        for i in range(1, n):
            start1, end1 = ans[-1]
            start2, end2 = intervals[i]

            if end1 >= start2:
                ans[-1] = [start1, max(end1, end2)]
            else:
                ans.append([start2, end2])
        
        return ans