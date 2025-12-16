# Last updated: 16.12.2025, 17:41:25
1class Solution:
2    def subarraySum(self, nums: List[int], k: int) -> int:
3        
4        prefix = {0:1}
5        curr = 0
6        count = 0
7        # k = 6 arr = 1 2 3 1 0 0 0 
8
9        for num in nums:
10            curr += num
11
12            if curr - k in prefix:
13                count += prefix[curr-k]
14
15            prefix[curr] = prefix.get(curr, 0) + 1
16
17        return count