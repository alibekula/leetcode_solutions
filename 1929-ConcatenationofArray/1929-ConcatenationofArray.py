# Last updated: 22.11.2025, 20:32:30
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)

        for i in range(n):
            nums.append(nums[i])
        
        return nums