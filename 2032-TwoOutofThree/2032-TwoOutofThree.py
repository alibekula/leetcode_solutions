# Last updated: 17.11.2025, 19:06:12
class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        
        sett1, sett2, sett3 = set(nums1), set(nums2), set(nums3)

        return list(sett1.intersection(sett2).union(sett1.intersection(sett3)).union(sett2.intersection(sett3)))