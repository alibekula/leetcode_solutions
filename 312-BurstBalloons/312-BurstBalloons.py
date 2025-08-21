# Last updated: 22.08.2025, 04:16:37
from collections import defaultdict 
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0]*n for i in range(n)]

        for length in range(2, n):
            for left in range(n-length):
                right = left + length
                for i in range(left+1, right):
                    dp[left][right] = max(dp[left][right], dp[left][i] + nums[left]*nums[i]*nums[right] + dp[i][right])
        
        return dp[0][n-1]