# Last updated: 13.08.2025, 17:00:38
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals

        intervals.sort(key=lambda x: x[0])
        r = 1
        ans = [intervals[0]]

        while r < len(intervals):
            if ans[-1][1] >= intervals[r][0]:
                ans[-1] = [ans[-1][0], max(ans[-1][1], intervals[r][1])]
            else:
                ans.append(intervals[r])

            r += 1

        return ans




        