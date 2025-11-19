# Last updated: 19.11.2025, 16:53:52
class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        
        sett = set(nums)

        while original in sett:
            original *= 2
        
        return original