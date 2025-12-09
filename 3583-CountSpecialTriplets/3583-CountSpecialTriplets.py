# Last updated: 09.12.2025, 15:24:48
1class Solution:
2    def specialTriplets(self, nums: List[int]) -> int:
3        
4        counter_all = {}
5        counter_left = {}
6        total = 0
7
8        for num in nums:
9            counter_all[num] = counter_all.get(num, 0) + 1
10        
11        n = len(nums)
12
13        for i in range(n):
14            num = nums[i]
15
16            left = counter_left.get(num *2, 0)
17            res = 1 if num == 0 else 0
18            right = max(0, counter_all.get(num*2, 0) - left - res)
19            total += left * right
20            counter_left[num] = counter_left.get(num, 0) + 1
21        
22        return total % (10 ** 9 + 7)
23
24