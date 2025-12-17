# Last updated: 17.12.2025, 21:02:24
1class Solution:
2    def maxDistToClosest(self, seats: List[int]) -> int:
3        # 0 0 0 0 0 1
4        # 1 0 0 0 0 0
5        # 1 0 0 0 0 1
6        # 0 0 1 0 0 1 0 0 0
7        # 0 1 2 3 4 5 6 7 8
8        # 0 
9        # 1
10        # 0 0 0 0 0 0
11        # 1 1 1 1 1 1
12        n = len(seats)
13        longest = 0
14        l, r = 0, 1
15
16        while r < n:
17
18            while r + 1 < n and seats[r] == 0:
19                r += 1
20            
21            if seats[r] == seats[l] == 1:
22                longest = max(longest, (r-l)//2)
23            else:
24                longest = max(longest, r-l)
25        
26            l = r
27            r += 1
28        
29        return longest