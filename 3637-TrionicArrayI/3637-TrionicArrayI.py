# Last updated: 03.02.2026, 23:35:01
1class Solution:
2    def isTrionic(self, nums: List[int]) -> bool:
3        
4        n = len(nums)
5        up = True
6        ans = []
7
8        if nums[0] > nums[1]:
9            return False
10
11        for j in range(1, n):
12            i = j-1
13
14            if nums[i] == nums[j]:
15                return False
16
17            if not up and nums[i] > nums[j]:
18                up = True
19                ans.append('v')
20            
21            if up and nums[i] < nums[j]:
22                up = False
23                ans.append('p')
24        
25        return ans == ['p', 'v', 'p']
26            
27
28
29