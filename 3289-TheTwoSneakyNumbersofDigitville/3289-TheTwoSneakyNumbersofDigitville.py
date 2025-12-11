# Last updated: 11.12.2025, 20:39:30
1class Solution:
2    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
3        
4        n = len(nums)-3
5        cumsum = n*(n+1)//2
6        squares = (n * (n+1) * (2*n + 1))//6
7
8        curr_cumsum = 0
9        curr_squares= 0
10
11        for num in nums:
12            curr_cumsum += num
13            curr_squares += num**2
14        
15        a_plus_b = curr_cumsum - cumsum
16        a2_plus_b2 = curr_squares - squares
17
18        a_mult_b = (a_plus_b ** 2 - a2_plus_b2)//2
19
20        ans = []
21
22        for i in range(0, n+1):
23            if i ** 2 - a_plus_b * i + a_mult_b == 0:
24                ans.append(i)
25            
26            if len(ans) == 2:
27                return ans
28
29
30