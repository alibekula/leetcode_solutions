# Last updated: 22.11.2025, 21:10:46
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        sett = set(nums)
        ans = []

        for i in range(1, len(nums)+1):
            if i not in sett:
                ans.append(i)

        return ans