# Last updated: 13.08.2025, 16:58:09
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        self.dp = [1]
        if len(self.dp) >= n:
            return self.dp[n-1]
        
        p, q, k = 0, 0, 0 

        while len(self.dp) < n:
            ugly = min(self.dp[p] * 2, self.dp[q] * 3, self.dp[k] * 5)
            self.dp.append(ugly)

            if ugly == self.dp[p] * 2:
                p += 1
            
            if ugly == self.dp[q] * 3:
                q += 1

            if ugly == self.dp[k] * 5:
                k += 1
        
        return self.dp[n-1]