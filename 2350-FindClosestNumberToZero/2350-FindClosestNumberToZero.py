# Last updated: 13.08.2025, 16:56:16
class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        res = nums[0]
        for i in nums[1:]:
            if abs(i) < abs(res):
                res = i
            elif abs(i) == abs(res) and i > res:
                res = i
        return res
        