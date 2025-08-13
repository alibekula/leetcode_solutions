# Last updated: 13.08.2025, 16:57:53
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        k = len(primes)
        dp = [1] * n
        indices = [0] * k
        
        for i in range(1, n):
            next_val = min(dp[indices[j]] * primes[j] for j in range(k))
            dp[i] = next_val
            for j in range(k):
                if dp[indices[j]] * primes[j] == next_val:
                    indices[j] += 1
        return dp[-1]
