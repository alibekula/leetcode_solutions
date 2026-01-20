# Last updated: 20.01.2026, 22:11:05
1class Solution:
2    def minBitwiseArray(self, nums: List[int]) -> List[int]:
3        ans = []
4
5        for num in nums:
6
7            if num % 2 == 0:
8                ans.append(-1)
9                continue
10
11            i = 0
12
13            while num >> i & 1:
14                i += 1
15
16            num = num & ~(1<<(i-1))
17            ans.append(num)
18        
19        return ans
20
21