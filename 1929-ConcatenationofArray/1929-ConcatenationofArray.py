# Last updated: 22.11.2025, 21:07:36
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        dct = {key: 0 for key in range(1, len(nums)+1)}

        ans = []

        for num in nums:
            dct[num] += 1

        for key, value in dct.items():
            if value == 0:
                ans.append(key)

        return ans