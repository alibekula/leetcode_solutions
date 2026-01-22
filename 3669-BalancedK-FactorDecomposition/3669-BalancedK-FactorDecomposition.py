# Last updated: 22.01.2026, 23:59:27
1class Solution:
2    def minDifference(self, n: int, k: int) -> List[int]:
3
4        tmp = n ** (1/k)
5
6        if tmp == int(tmp):
7            return [int(tmp) for _ in range(k)]
8        
9        def get_factors(num):
10
11            if num == 1:
12                return [1]
13
14            factors = []
15
16            for i in range(2, int(num ** 0.5) + 1):
17                
18                if i > num:
19                    break
20
21                factor = 1
22                while num % i == 0:
23                    num //= i
24                    factors.append(i)
25            
26            if num != 1: factors.append(num)
27
28            return factors
29        
30        factors = get_factors(n)
31
32        while len(factors) < k:
33            factors.append(1)
34
35        factors.sort()
36
37        if len(factors) == k:
38            return factors
39        
40        buckets = [1 for _ in range(k)]
41        min_diff = float('inf')
42        best_buckets = []
43
44        def backtrack(idx):
45            nonlocal min_diff, k, best_buckets
46
47            if idx == len(factors):
48                curr_max_diff = max(buckets) - min(buckets)
49
50                if curr_max_diff < min_diff:
51                    min_diff = curr_max_diff
52                    best_buckets = buckets[:]
53                
54                return
55            
56            prime = factors[idx]
57            seen = set()
58
59            for i in range(k):
60
61                if buckets[i] in seen:
62                    continue
63                
64                seen.add(buckets[i])
65
66                buckets[i] = buckets[i] * prime
67                backtrack(idx+1)
68                buckets[i] //= prime
69        
70        backtrack(0)
71
72        return best_buckets
73
74
75
76
77
78
79
80        
81
82