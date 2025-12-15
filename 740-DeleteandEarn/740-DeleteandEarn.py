# Last updated: 16.12.2025, 00:21:58
1
2class Solution:
3    def deleteAndEarn(self, nums: List[int]) -> int:
4        counter = {}
5        total = 0
6        for num in nums:
7            counter[num] = counter.get(num, 0) + 1
8        
9        deleted = []
10
11        for key in list(counter.keys()):
12            if key - 1 not in counter and key + 1 not in counter:
13                total += counter[key] * key
14                deleted.append(key)
15        
16        for key in deleted:
17            if key in counter:
18                del counter[key]
19
20        ranges = []
21        
22        sett = set(counter.keys())
23
24        for start in sett:
25            if start-1 not in sett:
26                end = start
27
28                while end + 1 in sett:
29                    end += 1
30                
31                ranges.append([start, end])
32            
33
34        for start, end in ranges:
35            
36            current_points = []
37            
38            for num_val in range(start, end + 1):
39                current_points.append(num_val * counter[num_val])
40                
41            dp = [0] * len(current_points)
42            dp[0] = current_points[0]
43            dp[1] = max(current_points[0], current_points[1])
44            
45            for i in range(2, len(current_points)):
46                dp[i] = max(dp[i - 1], dp[i - 2] + current_points[i])
47            
48            total += dp[-1]
49        
50        return total