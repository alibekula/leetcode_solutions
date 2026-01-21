# Last updated: 22.01.2026, 00:47:23
1class Solution:
2    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
3        
4        max_trim = max(queries, key=lambda x: x[1])[1]
5        min_trim = min(queries, key=lambda x: x[1])[1]
6        n = len(nums[0])
7        dct = {}
8
9        for i in range(min_trim, max_trim + 1):  
10            curr = []
11            for idx, num in enumerate(nums):
12                curr.append([int(num[n-i:]), idx])
13            
14            curr.sort()
15
16            dct[i] = curr[:]
17        
18        ans = []
19
20        for k, trim in queries:
21            ans.append(dct[trim][k-1][1])
22        
23        return ans