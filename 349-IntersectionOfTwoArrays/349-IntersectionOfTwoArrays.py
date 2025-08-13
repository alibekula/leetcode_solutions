# Last updated: 13.08.2025, 16:57:43
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1
        
        sett =set(nums2)
        ans = []

        for item in nums1:
            if item in sett:
                ans.append(item)
                sett.remove(item)
        
        return ans
        