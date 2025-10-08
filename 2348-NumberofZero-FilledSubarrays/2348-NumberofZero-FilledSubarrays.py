# Last updated: 08.10.2025, 19:23:14
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        
        n = len(nums)
        i = 0
        total = 0

        while i < n:
            num = nums[i]
            if num != 0:
                count = 0
            elif i > 0 and nums[i-1] == 0 and nums[i] == 0:
                count += 1
            else:
                count = 1
            i += 1
            total += count
        
        return total
            
