# Last updated: 06.02.2026, 11:42:41
1class Solution:
2    def minRemoval(self, nums: List[int], k: int) -> int:
3        
4        nums.sort()
5        n = len(nums)
6        longest = 1
7
8        def binsearch(arr, target):
9            l, r = 0, len(arr)-1
10            ans = float('-inf')
11
12            while l <= r:
13                mid = (l+r)//2
14
15                if arr[mid] <= target:
16                    ans = mid
17                    l = mid + 1
18                else:
19                    r = mid - 1
20            
21            return ans
22
23        for i in range(n-1):
24            num = nums[i]
25            r = binsearch(nums, num * k)
26            longest = max(r-i+1, longest)
27
28        return n - longest
29