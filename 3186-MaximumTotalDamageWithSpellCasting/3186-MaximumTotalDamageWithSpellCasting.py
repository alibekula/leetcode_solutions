# Last updated: 11.10.2025, 15:16:58
from collections import Counter
import bisect

class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        cnt = Counter(power)
        values = sorted(cnt)
        n = len(values)

        # damage[i] = общий урон, если взять все заклинания силы values[i]
        damage = [v * cnt[v] for v in values]

        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            # найти первый индекс j, где values[j] > values[i] + 2
            j = bisect.bisect_right(values, values[i] + 2)
            dp[i] = max(dp[i + 1], damage[i] + dp[j])

        return dp[0]
