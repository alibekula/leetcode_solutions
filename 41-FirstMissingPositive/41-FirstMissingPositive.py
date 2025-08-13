# Last updated: 13.08.2025, 17:00:52
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        n = len(nums)

        for i in range(n):

            while 1 <= nums[i] <= n and nums[nums[i]-1] != nums[i]:
                idx = nums[i] - 1

                nums[idx], nums[i] = nums[i], nums[idx]
        
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        return n + 1