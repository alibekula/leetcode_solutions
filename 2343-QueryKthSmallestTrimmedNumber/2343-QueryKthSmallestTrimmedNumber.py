# Last updated: 22.01.2026, 04:58:51
1class Solution:
2    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
3        
4        n = len(nums)
5        queries_map = {}
6        len_str = len(nums[0])
7        max_trim = 0
8        len_queries = len(queries)
9        ans = [0 for _ in range(len_queries)]
10
11        for idx, (k, trim) in enumerate(queries):
12            
13            if trim not in queries_map:
14                queries_map[trim] = []
15
16            queries_map[trim].append([k, idx])
17            max_trim = max(trim, max_trim)
18        
19        indices = list(range(n))
20        ans = [0 for _ in range(len_queries)]
21
22        for tr in range(1, max_trim+1):
23
24            pos = len_str - tr
25            buckets = [[] for _ in range(10)]
26
27            for i in indices:
28                num = nums[i][pos]
29                buckets[int(num)].append(i)
30            
31            indices = []
32
33            for bucket in buckets:
34                indices.extend(bucket)
35            
36            if tr in queries_map:
37                for k, idx in queries_map[tr]:
38                    ans[idx] = indices[k-1]
39        
40        return ans
41
42            
43
44
45
46
47
48
49