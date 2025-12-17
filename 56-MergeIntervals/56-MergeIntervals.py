# Last updated: 17.12.2025, 21:13:24
1class Solution:
2    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
3        intervals.sort()
4        # 1 - 3 1 - 2
5        n = len(intervals)
6        if n <= 1:
7            return intervals
8                
9        ans = [intervals[0]]
10
11        for i in range(1, n):
12            left = ans[-1]
13            right = intervals[i]
14
15            if left[1] >= right[0]:
16                ans[-1] = [left[0], max(right[1], left[1])]
17            else:
18                ans.append(right)
19        
20        return ans
21
22        
23