# Last updated: 13.08.2025, 16:58:08
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0

        for i in range(len(nums)+1):
            res += i
        
        tmp = 0

        for j in nums:
            tmp += j

        return res - tmp