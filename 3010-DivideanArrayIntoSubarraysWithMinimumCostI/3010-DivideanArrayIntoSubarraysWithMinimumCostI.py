# Last updated: 01.02.2026, 17:40:17
1class Solution:
2    def minimumCost(self, nums: List[int]) -> int:
3        a, b, c = nums[0], min(nums[1], nums[2]), max(nums[1], nums[2])
4        n = len(nums)
5        # 1 5 100 4 3 
6        for i in range(3, n):
7            if nums[i] < b:
8                b, c = nums[i], b
9            elif nums[i] < c:
10                c = nums[i]
11        
12        return a + b + c