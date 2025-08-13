# Last updated: 13.08.2025, 16:58:37
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        n = len(nums)
        prev_l, then_l = 0, 0
        prev_r, then_r = 0, 0

        for idx, curr in enumerate(nums):
            if idx != n-1:
                prev_l, then_l = then_l, max(prev_l+curr, then_l)
            
            if idx != 0:
                prev_r, then_r = then_r, max(prev_r+curr, then_r)
        
        return max(then_r, then_l)

                

            