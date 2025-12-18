# Last updated: 18.12.2025, 17:52:34
1class Solution:
2    def maxPower(self, s: str) -> int:
3        n = len(s)
4
5        if n <= 1:
6            return n
7        
8        longest = 1
9        curr = 1
10        for j in range(1, n):
11            i = j-1
12            if s[i] == s[j] or j == n-1:
13                curr += 1 if s[i] == s[j] else 0
14                longest = max(longest, curr)
15            
16            else:
17                curr = 1
18        
19        return longest
20
21        