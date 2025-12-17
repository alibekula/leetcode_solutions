# Last updated: 17.12.2025, 22:11:11
1class Solution:
2    from collections import Counter
3    def findAnagrams(self, s: str, p: str) -> List[int]:
4        counter = Counter(p)
5        window = Counter(s[:len(p)])
6
7        prev = 0
8        ans = []
9
10        if counter == window:
11            ans.append(0)
12
13        for char in s[len(p):]:
14            window[s[prev]] -= 1
15
16            if window[s[prev]] == 0:
17                del window[s[prev]]
18
19            prev += 1
20
21            if char not in window:
22                window[char] = 0
23
24            window[char] += 1
25
26            if window == counter:
27                ans.append(prev)
28        
29        return ans 
30