# Last updated: 13.08.2025, 16:58:03
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros = 0
        nonzero_pos = 0
        l = 0

        while l < len(nums):
            if nums[l] != 0:
                nums[nonzero_pos] = nums[l]
                nonzero_pos += 1
            else:
                zeros += 1
            l += 1
        
        for j in range(nonzero_pos, len(nums)):
            nums[j] = 0
        
        return nums

        