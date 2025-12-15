# Last updated: 16.12.2025, 01:06:10
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
22
23        for start in counter:
24            if start-1 not in counter:
25                end = start
26
27                while end + 1 in counter:
28                    end += 1
29                
30                ranges.append([start, end])
31            
32
33        for start, end in ranges:
34            
35            current_points = []
36            
37            for num_val in range(start, end + 1):
38                current_points.append(num_val * counter[num_val])
39                
40            dp = [0] * len(current_points)
41            dp[0] = current_points[0]
42            dp[1] = max(current_points[0], current_points[1])
43            
44            for i in range(2, len(current_points)):
45                dp[i] = max(dp[i - 1], dp[i - 2] + current_points[i])
46            
47            total += dp[-1]
48        
49        return total