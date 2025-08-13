# Last updated: 13.08.2025, 16:58:34
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        sett = set()
        for n in nums:
            if n in sett:
                return True
            else:
                sett.add(n)
        return False
        