# Last updated: 16.12.2025, 17:49:35
1class Solution:
2    def moveZeroes(self, nums: List[int]) -> None:
3        """
4        Do not return anything, modify nums in-place instead.
5        """
6        zeros_count = 0
7        p = 0
8        n = len(nums)
9        # 0 1 2 0 3 4 0 5 6
10
11        for i in range(n):
12            if nums[i] == 0:
13                zeros_count += 1
14            else:
15                nums[p] = nums[i]
16                p += 1
17        
18        for j in range(n-1, n-zeros_count-1,-1):
19            nums[j] = 0
20
21        
22
23        