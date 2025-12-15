# Last updated: 15.12.2025, 20:54:05
1import random
2
3class Solution:
4    def absDifference(self, nums: list[int], k: int) -> int:
5        
6        def get_sum_smallest_k(arr, k):
7            if not arr: 
8                return 0
9
10            pivot = random.choice(arr)
11
12            left = [ x for x in arr if x < pivot]
13            mid = [x for x in arr if x == pivot]
14            right = [ x for x in arr if x > pivot]
15
16            if len(left) >= k:
17                if len(left) == k:
18                    return sum(left)
19                else:
20                    return get_sum_smallest_k(left, k)
21            elif len(left) + len(mid) >= k:
22                if len(mid) + len(left) == k:
23                    return sum(mid) + sum(left)
24                else:
25                    return sum(left) + pivot * (k - len(left))
26            else:
27                return sum(left) + sum(mid) + get_sum_smallest_k(right, k - len(left) - len(mid))\
28        
29        sum_left = get_sum_smallest_k(nums, k)
30
31        arr = [-x for x in nums]
32        sum_right = -get_sum_smallest_k(arr, k)
33
34        return sum_right - sum_left