# Last updated: 21.08.2025, 18:20:32
from collections import defaultdict 
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        
        n = len(nums)
        nums = [1] + nums + [1]
        memo = defaultdict(int)

        def solve(left, right):
            if left+1 == right:
                return 0
            if (left, right) in memo:
                return memo[(left, right)]
            
            ans = float('-inf')
            for i in range(left+1, right):
                curr = nums[left] * nums[i] * nums[right] + solve(left, i) + solve(i, right)

                ans = max(curr, ans, 0)
            

            memo[(left, right)] = ans

            return ans
        
        return solve(0, len(nums)-1)
