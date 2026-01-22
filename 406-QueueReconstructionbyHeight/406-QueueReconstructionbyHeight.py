# Last updated: 23.01.2026, 02:53:25
1class Solution:
2    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
3        
4        dct = {}
5
6        for h, k in people:
7            if h not in dct:
8                dct[h] = []
9            
10            dct[h].append(k)
11        
12        n = len(people)
13        nums = list(dct.keys())
14        nums.sort()
15        ans = [None for _ in range(n)]
16
17        for key in dct:
18            dct[key].sort()
19
20        for h in nums:
21            prev_count = 0
22            pos = 0
23
24            for k in dct[h]:
25                while pos < n:
26                    
27                    if prev_count == k and ans[pos] is None:
28                        ans[pos] = [h, k]
29                        prev_count += 1
30                        break
31                    if ans[pos] is None:
32                        prev_count += 1
33
34                    pos += 1
35        return ans
36
37
38
39