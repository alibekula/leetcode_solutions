# Last updated: 25.01.2026, 22:39:38
1class Solution:
2    def minimumDifference(self, nums: List[int], k: int) -> int:
3        
4        if k == 1:
5            return 0
6
7        nums.sort()
8        l, r = 0, k-1
9        min_diff = float('inf')
10        n = len(nums)
11
12        while r < n:
13            min_diff = min(min_diff, nums[r]-nums[l])
14            l += 1
15            r += 1
16
17        return min_diff
18