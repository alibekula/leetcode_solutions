# Last updated: 23.01.2026, 00:09:36
1class Solution:
2    def minDifference(self, n: int, k: int, best=float('inf')) -> List[int]:
3        
4        if k == 1: return [n]
5
6        for cand in range(1, ceil(n**(1/k))+1):
7
8            if n % cand != 0: continue
9
10            divs = self.minDifference(n//cand, k-1)
11            divs.append(cand)
12            mn, mx = min(divs), max(divs)
13
14            if best > mx-mn:
15                best, ans = mx-mn, divs
16        
17        return ans