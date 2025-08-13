# Last updated: 13.08.2025, 17:01:35
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dct = {}

        for idx, num in enumerate(nums):

            if target - num in dct:
                return [dct[target - num], idx] 
            else:
                dct[num] = idx