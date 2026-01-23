# Last updated: 23.01.2026, 21:16:36
1class Solution:
2    def minimumPairRemoval(self, nums: List[int]) -> int:
3        # 5 2 3 1        
4        n = len(nums) # 4
5        active = [True for _ in range(n)]
6        left = [i if i != -1 else None for i in range(-1, n-1)] # none 0 1 2
7        right = [i if i != n else None for i in range(1, n+1)] # 1 2 3 none
8
9        heap = []
10        bad_pairs = 0
11
12        for j in range(1, n):
13            i = j-1
14            if nums[i] > nums[j]:
15                bad_pairs += 1 # 2
16            heapq.heappush(heap, [nums[i] + nums[j], i, j])
17        
18        if bad_pairs == 0:
19            return 0
20        
21        ops = 0
22        while heap:
23            
24            if bad_pairs == 0:
25                return ops
26
27            val, i, j = heapq.heappop(heap)
28
29            if active[i] and active[j] and nums[i] + nums[j] == val:
30
31                ops += 1
32
33                if nums[i] > nums[j]:
34                    bad_pairs -= 1
35
36                if left[i] is not None:
37                    l = nums[left[i]] # l = 1 nums[i] = 3, val =4
38
39                    if l > nums[i] and l <= val:
40                        bad_pairs -=1
41                    elif l <= nums[i] and l > val:
42                        bad_pairs += 1
43                
44                if right[j] is not None:
45                    r = nums[right[j]]
46
47                    if r >= nums[j] and r < val:
48                        bad_pairs += 1
49                    elif r < nums[j] and r >= val:
50                        bad_pairs -= 1
51
52                    right[i] = right[j]
53                    left[right[j]] = i
54
55                else:
56                    right[i] = None
57                
58                
59                if right[i] is not None:
60                    heapq.heappush(heap, [val + nums[right[i]], i, right[i]])
61                
62                if left[i] is not None:
63                    heapq.heappush(heap, [val + nums[left[i]], left[i], i])
64                
65                nums[i] = val
66                active[j] = False
67        
68        return ops
69        
70