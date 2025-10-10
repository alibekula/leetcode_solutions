# Last updated: 10.10.2025, 14:22:55
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dct = {}

        for idx, num in enumerate(nums):

            if target - num in dct:
                return [dct[target - num], idx] 
            else:
                dct[num] = idx