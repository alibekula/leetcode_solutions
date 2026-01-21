# Last updated: 21.01.2026, 23:16:11
1class Solution:
2    def minBitwiseArray(self, nums: List[int]) -> List[int]:
3        ans = []
4        # 0 0 0 1 1 0 0 0 1 1 1
5        # 0 0 0 1 1 0 0 0 1 1 0
6        # 0 1 1 1
7        # 0 0 1 1 | 0 1 0 0 
8        # 0 1 0 1 
9        # 0 1 0 0 | 0 1 0 1
10        # 1 1 0 1
11        # 1 1 0 0 | 1 1 0 1
12        
13        for num in nums:
14
15            if num == 2:
16                ans.append(-1)
17                continue
18
19            i = 0
20            
21            while num >> i & 1:
22                i += 1
23            
24            num = num & ~(1 << (i-1))
25
26            ans.append(num)
27        
28        return ans