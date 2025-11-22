# Last updated: 22.11.2025, 20:20:51
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
        res = 0

        for num in nums:
            residual = num %3
            res += min(3-residual, residual)
        
        return res
        