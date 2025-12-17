# Last updated: 17.12.2025, 20:26:34
1class Solution:
2    def maxDistToClosest(self, seats: List[int]) -> int:
3        
4        l, r = 0, 0
5        n = len(seats)
6        longest = 0
7        # 0 1 2 3 4 5 6
8        # 0 0 0 0 0 0 1 +
9        # 1 0 0 0 0 0 0 +
10        # 1 1 1 1 0 0 0 +
11        # 1 0 0 0 0 0 1 
12
13        while r < n-1:
14
15            while seats[r] != 1:
16                r += 1
17
18                if r == n-1:
19                    break
20                
21            if seats[r] == 1 and seats[l] == 1:
22                longest = max(longest, (r-l) // 2)
23            else:
24                longest = max(longest, r-l)
25            
26            l = r
27            r += 1
28        
29        return longest