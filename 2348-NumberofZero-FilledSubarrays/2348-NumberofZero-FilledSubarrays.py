# Last updated: 08.10.2025, 19:20:57
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        
        zeros = []
        n = len(nums)
        i = 0

        while i < n:
            num = nums[i]
            if num != 0:
                count = 0
            elif i > 0 and nums[i-1] == 0 and nums[i] == 0:
                count += 1
            else:
                count = 1
            i += 1
            zeros.append(count)
        
        total = 0

        for c in zeros:
            if c != 0:
                total += c
        
        return total
