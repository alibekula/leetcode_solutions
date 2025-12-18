# Last updated: 18.12.2025, 16:55:32
1class Solution:
2    def lengthOfLongestSubstring(self, s: str) -> int:
3        # abcabc
4        if len(s) == 0:
5            return 0
6
7        sett = set(s[0])
8        longest = 1
9        n = len(s)
10        l, r = 0, 1
11
12        while r < n:
13
14            while r < n and s[r] not in sett:
15                sett.add(s[r])
16                longest = max(longest, r-l+1)
17                r += 1
18            
19            while r < n and l < r and s[r] in sett:
20                sett.remove(s[l])
21                l += 1
22        
23        return longest
24
25