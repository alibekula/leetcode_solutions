# Last updated: 21.01.2026, 03:53:22
1class Solution:
2    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
3        n, m = len(mat), len(mat[0])
4
5        if threshold == 0:
6            return min(n, m)
7
8        prefix = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
9
10        for i in range(1, n+1):
11            for j in range(1, m+1):
12                prefix[i][j] = prefix[i-1][j] + prefix[i][j-1] + mat[i-1][j-1] - prefix[i-1][j-1]
13
14
15        def is_valid(size):
16
17            for i in range(1, n-size + 2):
18                for j in range(1, m-size + 2):
19                    curr = prefix[size + i - 1][size + j - 1]
20                    top = prefix[i-1][size + j - 1]
21                    left = prefix[size + i - 1][j-1]
22                    intersect = prefix[i-1][j-1]
23                    total = curr - top - left + intersect
24
25                    if total <= threshold:
26                        return True
27            
28            return False
29        
30        ans = 0
31
32        def binsearch():
33            nonlocal ans
34            l, r = 2, min(n, m)
35
36            if not is_valid(1):
37                return 0
38            else:
39                ans = 1
40            
41            while l <= r:
42                mid = (l+r)//2
43
44                if is_valid(mid):
45                    l = mid + 1
46                    ans = mid
47                else:
48                    r = mid - 1
49        
50        binsearch()
51        return ans
52
53
54
55