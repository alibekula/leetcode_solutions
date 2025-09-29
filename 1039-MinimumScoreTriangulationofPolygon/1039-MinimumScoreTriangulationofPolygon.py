# Last updated: 29.09.2025, 08:44:15
class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        from functools import lru_cache
        n = len(values)

        @lru_cache(None)
        def dfs(i, j):
            if j - i < 2:
                return 0

            ans = float('inf')
            for k in range(i + 1, j):
                cost = dfs(i, k) + dfs(k, j) + values[i] * values[j] * values[k]
                ans = min(ans, cost)

            return ans

        return dfs(0, n - 1)
