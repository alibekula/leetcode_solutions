# Last updated: 15.12.2025, 20:32:50
1import random
2
3class Solution:
4    def absDifference(self, nums: list[int], k: int) -> int:
5        
6        def get_sum_smallest_k(arr, k):
7            if not arr: return 0
8            
9            pivot = random.choice(arr)
10            
11            left = [x for x in arr if x < pivot] 
12            mid = [x for x in arr if x == pivot]  
13            right = [x for x in arr if x > pivot] 
14            
15            len_l = len(left)
16            len_m = len(mid)
17            
18            if k <= len_l:
19                return get_sum_smallest_k(left, k)
20            elif k <= len_l + len_m:
21                return sum(left) + pivot * (k - len_l)
22            else:
23                return sum(left) + sum(mid) + get_sum_smallest_k(right, k - len_l - len_m)
24        
25        sum_min = get_sum_smallest_k(nums, k)
26        
27
28        neg_nums = [-x for x in nums]
29        sum_max_neg = get_sum_smallest_k(neg_nums, k)
30        sum_max = -sum_max_neg
31        
32        return abs(sum_max - sum_min)