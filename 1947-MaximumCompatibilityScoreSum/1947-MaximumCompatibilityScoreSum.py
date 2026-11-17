# Last updated: 17.11.2026, 12:11:03
1
2class Solution:
3    def maxCompatibilitySum(self, students, mentors):
4        n = len(students)
5
6        cost = [
7            [-sum(a == b for a, b in zip(s, m)) for m in mentors]
8            for s in students
9        ]
10
11        u = [0] * (n + 1)
12        v = [0] * (n + 1)
13        p = [0] * (n + 1)
14        way = [0] * (n + 1)
15
16        for i in range(1, n + 1):
17            p[0] = i
18            j0 = 0
19            used = [False] * (n + 1)
20            minv = [float("inf")] * (n + 1)
21
22            while True:
23                used[j0] = True
24                i0 = p[j0]
25                delta = float("inf")
26                j1 = 0
27
28                for j in range(1, n + 1):
29                    if used[j]:
30                        continue
31
32                    cur = cost[i0 - 1][j - 1] - u[i0] - v[j]
33
34                    if cur < minv[j]:
35                        minv[j] = cur
36                        way[j] = j0
37
38                    if minv[j] < delta:
39                        delta = minv[j]
40                        j1 = j
41
42                for j in range(n + 1):
43                    if used[j]:
44                        u[p[j]] += delta
45                        v[j] -= delta
46                    else:
47                        minv[j] -= delta
48
49                j0 = j1
50
51                if p[j0] == 0:
52                    break
53
54            while True:
55                j1 = way[j0]
56                p[j0] = p[j1]
57                j0 = j1
58
59                if j0 == 0:
60                    break
61
62        return -sum(cost[p[j] - 1][j - 1] for j in range(1, n + 1))
63