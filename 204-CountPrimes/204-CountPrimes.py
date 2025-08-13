# Last updated: 13.08.2025, 16:58:48
class Solution:
    def countPrimes(self, n: int) -> int:
        lp = [0] * n  # We only need indices 0..n-1
        pr = []
        
        for i in range(2, n):  # iterate from 2 to n-1 (primes less than n)
            if lp[i] == 0:
                pr.append(i)
                lp[i] = i
            for p in pr:
                if p > lp[i] or p * i >= n:
                    break
                lp[p * i] = p
        
        return len(pr)