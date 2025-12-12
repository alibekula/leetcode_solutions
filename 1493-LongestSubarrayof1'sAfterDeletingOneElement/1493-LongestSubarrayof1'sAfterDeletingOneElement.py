# Last updated: 12.12.2025, 21:28:37
1class Solution:
2    def longestSubarray(self, nums: List[int]) -> int:
3        longest = 0
4
5        l, r = 0, 0
6        zeros = 0
7
8        while r < len(nums):
9
10            while r < len(nums) and (nums[r] != 0 or zeros == 0):
11                if nums[r] == 0:
12                    zeros += 1
13                
14                longest = max(longest, r-l)
15                r += 1
16            
17            while l < r and zeros == 1:
18                if nums[l] == 0:
19                    zeros -= 1
20                
21                l += 1
22        
23        return longest
24