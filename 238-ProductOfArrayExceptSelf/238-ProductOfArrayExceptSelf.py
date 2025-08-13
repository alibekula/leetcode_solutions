# Last updated: 13.08.2025, 16:58:17
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        ans = [1] * n
        pref = 1
        suff = 1

        for i in range(n):
            ans[i] *= pref
            pref *= nums[i]
        
        for j in range(n-1, -1, -1):
            ans[j] *= suff
            suff *= nums[j]
        
        return ans