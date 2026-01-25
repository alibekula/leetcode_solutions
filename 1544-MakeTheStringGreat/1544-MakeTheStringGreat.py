# Last updated: 26.01.2026, 01:08:02
1class Solution:
2    def makeGood(self, s: str) -> str:
3
4        stack = []
5        n = len(s)
6        if n == 1:
7            return s
8
9        nei = {}
10
11        for i in range(n):
12            left = None if i == 0 else i-1
13            right = None if i == n-1 else i+1
14
15            nei[i] = [left, right]
16
17        
18        big = set(chr(i) for i in range(ord('Z'), ord('A')-1, -1))
19        small = set(chr(i) for i in range(ord('z'), ord('a')-1, -1))
20
21        def check(a, b):
22            if ((a in big and b in small) or (a in small and b in big)) and (a.lower() == b.lower()):
23                return True
24            return False
25        
26        active = [True for _ in range(n)]
27
28        for idx in nei:
29            left, right = nei[idx]
30
31            if not active[idx]:
32                continue
33
34            if left is not None and active[left]:
35                if check(s[idx], s[left]):
36                    active[idx] = False
37                    active[left] = False
38                
39                    left_left = nei[left][0]
40                    if left_left is not None:
41                        nei[left_left][1] = right
42                        
43                    if right is not None:
44                        nei[right][0] = left_left
45
46            if not active[idx]:
47                continue
48
49            if right is not None and active[right]:
50                if check(s[idx], s[right]):
51                    active[idx] = False
52                    active[right] = False
53                
54                    right_right = nei[right][1]
55
56                    if right_right is not None:
57                        nei[right_right][0] = left
58
59                    if left is not None:
60                        nei[left][1] = right_right
61        
62        ans = []
63
64        for idx in range(n):
65            if active[idx]:
66                ans.append(s[idx])
67        
68        return ''.join(ans)