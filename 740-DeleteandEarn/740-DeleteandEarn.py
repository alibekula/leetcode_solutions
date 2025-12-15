# Last updated: 16.12.2025, 00:20:31
1from collections import Counter
2from typing import List
3
4class Solution:
5    def deleteAndEarn(self, nums: List[int]) -> int:
6        counter = {}
7        total = 0
8        for num in nums:
9            counter[num] = counter.get(num, 0) + 1
10        
11        deleted = []
12
13        for key in list(counter.keys()):
14            if key - 1 not in counter and key + 1 not in counter:
15                total += counter[key] * key
16                deleted.append(key)
17        
18        for key in deleted:
19            if key in counter:
20                del counter[key]
21
22        ranges = []
23        
24        sorted_keys = sorted(counter.keys())
25
26        for start in sorted_keys:
27            if start not in counter:
28                continue
29
30            if start - 1 not in counter:
31                end = start
32                while end + 1 in counter:
33                    end += 1
34                ranges.append((start, end))
35
36        for start, end in ranges:
37            
38            current_points = []
39            
40            for num_val in range(start, end + 1):
41                current_points.append(num_val * counter[num_val])
42                
43            dp = [0] * len(current_points)
44            dp[0] = current_points[0]
45            dp[1] = max(current_points[0], current_points[1])
46            
47            for i in range(2, len(current_points)):
48                dp[i] = max(dp[i - 1], dp[i - 2] + current_points[i])
49            
50            total += dp[-1]
51        
52        return total