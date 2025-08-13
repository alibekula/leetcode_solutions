# Last updated: 13.08.2025, 16:58:54
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0 for _ in range(n +2)]
        max_val = 0

        for i in range(2, n+2):
            max_val = max(nums[i-2] + dp[i-2], dp[i-1])
            dp[i] = max_val
        
        return dp[-1]