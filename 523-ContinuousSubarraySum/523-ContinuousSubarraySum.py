# Last updated: 11.10.2025, 13:34:03
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        total = 0
        residuals = {0:-1}

        if k == 0:
            return False

        for i in range(len(nums)):

            total += nums[i]

            total = total % k

            if total in residuals:
                if i - residuals[total] >= 2:
                    return True
            else:
                residuals[total] = i
        
        return False



        