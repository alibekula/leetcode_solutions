# Last updated: 22.01.2026, 19:41:10
1import heapq
2
3class Solution:
4    def minimumPairRemoval(self, nums: List[int]) -> int:
5        n = len(nums)
6        if n < 2:
7            return 0
8            
9        right = list(range(1, n + 1))
10        left = list(range(-1, n - 1))
11        active = [True] * n
12        
13        bad_pairs = 0
14        for i in range(n - 1):
15            if nums[i] > nums[i+1]:
16                bad_pairs += 1
17                
18        if bad_pairs == 0:
19            return 0
20
21        heap = []
22        for i in range(n - 1):
23            heapq.heappush(heap, (nums[i] + nums[i+1], i, i+1))
24            
25        ops = 0
26        
27        while heap:
28            val, i, j = heapq.heappop(heap)
29            
30            if not active[i] or not active[j] or right[i] != j:
31                continue
32            
33            if nums[i] + nums[j] != val:
34                continue
35            
36            l = left[i]
37            if l != -1:
38                if nums[l] > nums[i]: bad_pairs -= 1
39            
40            if nums[i] > nums[j]: bad_pairs -= 1
41            
42            r = right[j]
43            if r != n:
44                if nums[j] > nums[r]: bad_pairs -= 1
45
46            nums[i] = val     
47            active[j] = False 
48            ops += 1
49            
50            right[i] = r
51            if r != n:
52                left[r] = i
53
54            if l != -1:
55                if nums[l] > nums[i]: bad_pairs += 1
56                heapq.heappush(heap, (nums[l] + nums[i], l, i))
57            
58            if r != n:
59                if nums[i] > nums[r]: bad_pairs += 1
60                heapq.heappush(heap, (nums[i] + nums[r], i, r))
61
62            if bad_pairs == 0:
63                return ops
64
65        return ops