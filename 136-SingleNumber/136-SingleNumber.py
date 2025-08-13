# Last updated: 13.08.2025, 16:59:23
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if not nums:
            return 

        num= nums[0]

        for i in range(1, len(nums)):
            num ^= nums[i]
        
        return num