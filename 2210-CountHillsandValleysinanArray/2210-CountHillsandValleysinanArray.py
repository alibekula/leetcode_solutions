# Last updated: 22.01.2026, 20:34:40
1class Solution:
2    def countHillValley(self, nums: List[int]) -> int:
3        
4        n = len(nums)
5
6        l, m, r = 0, 1, 2
7        total = 0
8
9        arr = []
10
11        for j in range(1, n):
12            i = j- 1
13            if nums[i] != nums[j]:
14                arr.append(nums[i])
15            
16            if j == n-1:
17                arr.append(nums[j])
18
19        
20        nums = arr
21        n = len(nums)
22
23        while r < n:
24
25            if nums[l] < nums[m] > nums[r]:
26                total += 1
27            elif nums[l] > nums[m] < nums[r]:
28                total += 1
29
30            l, m, r = l+1, m+1, r+1
31        
32        return total
33
34
35        
36
37            