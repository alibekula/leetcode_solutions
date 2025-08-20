# Last updated: 21.08.2025, 02:58:55
class Solution:

    def count(self, s: str) -> tuple[int]:
        num_zeros = 0
        num_ones = 0

        for char in s:
            if char == '0':
                num_zeros += 1
            else:
                num_ones += 1
        
        return (num_zeros, num_ones)

    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        
        weights = [self.count(s) for s in strs]
        k = len(strs)

        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

        for zeros, ones in weights:
            for i in range(m, zeros-1, -1):
                for j in range(n, ones-1, -1):
                    dp[i][j] = max(dp[i-zeros][j-ones] + 1, dp[i][j])

        return dp[m][n]
        
