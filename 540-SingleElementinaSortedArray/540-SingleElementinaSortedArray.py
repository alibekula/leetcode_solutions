# Last updated: 11.12.2025, 17:48:40
1class Solution:
2    def singleNonDuplicate(self, nums: List[int]) -> int:
3        
4        if len(nums) == 1:
5            return nums[0]
6        
7        # 1 1 5 7 7 8 8 9 9
8
9        l, r = 0, len(nums)-1
10
11        while l <= r:
12            mid = (l+r) //2
13
14            if r - l <= 2:
15                if r == l:
16                    return nums[l]
17                if nums[mid] == nums[mid-1]:
18                    return nums[r]
19                else:
20                    return nums[l]
21            
22
23            if nums[mid] == nums[mid-1]:
24                left = mid-1
25                right = mid
26            elif nums[mid] == nums[mid+1]:
27                left = mid
28                right = mid-1
29            else:
30                return mid
31            
32            if left % 2 == 1:
33                r = mid-1
34            else:
35                l = mid+1
36