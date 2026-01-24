# Last updated: 24.01.2026, 23:06:25
1class Solution:
2    def minPairSum(self, nums: List[int]) -> int:
3        
4        nums.sort()
5        n = len(nums)
6
7        max_pair = float('-inf')
8        l, r = 0, n-1
9
10        while l < r:
11            pair = nums[l] + nums[r]
12
13            max_pair = max(max_pair, pair)
14            l += 1
15            r -= 1
16        
17        return max_pair
18