# Last updated: 24.01.2026, 23:31:57
1class Solution:
2    def waysToSplitArray(self, nums: List[int]) -> int:
3        
4        n = len(nums)
5        prefix = [0 for _ in range(n)]
6        prefix[0] = nums[0]
7
8        for j in range(1, n):
9            prefix[j] = prefix[j-1] + nums[j]
10        
11        total = 0 
12        for i in range(n-1):
13            left = prefix[i]
14            right = prefix[-1] - prefix[i]
15
16            if left >= right:
17                total += 1
18        
19        return total