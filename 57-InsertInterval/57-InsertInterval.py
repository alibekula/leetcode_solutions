# Last updated: 13.08.2025, 17:00:37
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Step 1: Binary search to find the insertion point
        l, r = 0, len(intervals)
        while l < r:
            mid = (l + r) // 2
            if intervals[mid][0] < newInterval[0]:
                l = mid + 1
            else:
                r = mid

        # Insert newInterval at the found position
        intervals.insert(l, newInterval)

        # Step 2: Merge intervals only in the affected range
        # Start merging from the interval before `l` if it exists
        start = max(0, l)
        result = intervals[:start]

        for i in range(start, len(intervals)):
            if not result or result[-1][1] < intervals[i][0]:
                result.append(intervals[i])  # No overlap
            else:
                result[-1][1] = max(result[-1][1], intervals[i][1])  # Merge overlap

        return result
