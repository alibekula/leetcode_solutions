# Last updated: 17.12.2025, 21:29:21
1class Solution:
2    def trap(self, height: List[int]) -> int:
3        
4        n = len(height)
5        l, r = 0, n-1
6        total = 0
7        left_max, right_max = 0, 0
8
9        while l < r:
10            left_height = height[l]
11            right_height = height[r]
12
13            left_max = max(left_max, left_height)
14            right_max = max(right_max, right_height)
15            curr_min_max = min(left_max, right_max)
16
17            if left_height <= right_height:
18                total += max(0, curr_min_max - left_height)
19                l += 1
20            else:
21                total += max(0, curr_min_max - right_height)
22                r -= 1
23        
24        return total
25