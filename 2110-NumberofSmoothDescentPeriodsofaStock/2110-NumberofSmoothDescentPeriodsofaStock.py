# Last updated: 15.12.2025, 20:17:14
1class Solution:
2    def getDescentPeriods(self, prices: List[int]) -> int:
3        n = len(prices)
4        total = 0
5        stack = []
6
7        for i in range(n):
8            # 4 3 2 1 8 2 
9            if not stack or stack[-1] -1 == prices[i]:
10                stack.append(prices[i])
11                total += len(stack)
12            else:
13                stack = [prices[i]]
14                total += 1
15        
16        return total
17