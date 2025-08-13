# Last updated: 13.08.2025, 17:01:09
class Solution:
        
    def removeDuplicates(self, nums: list[int]) -> int:
        l, r, idx = 0, 0, 0

        while r < len(nums):
            l = r
            while r < len(nums) and nums[l] == nums[r]:
                r += 1
            nums[idx] = nums[l]
            idx += 1 

        nums[:] = nums[:idx]

        return idx + 1