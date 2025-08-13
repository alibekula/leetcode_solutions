# Last updated: 13.08.2025, 16:56:15
from typing import List

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        # If right is less than the first prime, return no valid pair.
        if right < 2:
            return [-1, -1]
        # Ensure left starts at least at 2.
        left = max(left, 2)

        pr = []
        lp = [0 for i in range(right + 1)]
        
        # Linear sieve to generate primes up to 'right'
        for j in range(2, len(lp)):
            if lp[j] == 0:
                pr.append(j)
            for p in pr:
                if j * p >= len(lp):
                    break
                lp[j * p] = p
                if j % p == 0:
                    break
        
        # Binary search to return the left insertion index
        def bin_search(seq, target):
            l, r = 0, len(seq) - 1
            while l <= r:
                mid = (l + r) // 2
                if seq[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return l
        
        left_idx = bin_search(pr, left)
        # For right index, find insertion index for right+1 then subtract one.
        right_idx = bin_search(pr, right + 1) - 1

        # If there are less than two primes in the interval, return no valid pair.
        if right_idx - left_idx < 1:
            return [-1, -1]

        min_dist = [float('inf'), None, None]
        for pos in range(left_idx, right_idx):
            gap = pr[pos+1] - pr[pos]
            if gap < min_dist[0]:
                min_dist = [gap, pr[pos], pr[pos+1]]
            
            if min_dist in [1, 2]:
                return [min_dist[1], min_dist[2]]
        
        return [min_dist[1], min_dist[2]]