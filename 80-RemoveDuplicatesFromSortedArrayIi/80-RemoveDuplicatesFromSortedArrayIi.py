# Last updated: 13.08.2025, 17:00:11
class Solution:
        
    def removeDuplicates(self, nums: list[int]) -> int:
        j = 1
        count = 0
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                count += 1
            else:
                count = 0
            if count <=1:
                nums[j] = nums[i]
                j += 1
        return j