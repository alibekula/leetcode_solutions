# Last updated: 13.08.2025, 16:56:58
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)+1
        prev, curr = 0, 0
        for i in range(2, n):
            prev, curr = curr, min(prev+cost[i-2], curr+cost[i-1])
        return curr
        