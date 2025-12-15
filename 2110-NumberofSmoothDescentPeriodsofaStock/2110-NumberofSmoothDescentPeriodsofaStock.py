# Last updated: 15.12.2025, 20:20:31
1class Solution:
2    def getDescentPeriods(self, prices: List[int]) -> int:
3        n = len(prices)
4        total = 0
5        last = None
6        length = 0
7
8        for i in range(n):
9            # 4 3 2 1 8 2 
10            if last is None or last-1 == prices[i]:
11                length += 1
12                last = prices[i]
13                total += length
14            else:
15                last = prices[i]
16                total += 1
17                length = 1
18        
19        return total
20