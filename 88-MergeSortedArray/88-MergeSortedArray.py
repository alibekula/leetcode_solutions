# Last updated: 13.08.2025, 17:00:04
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l, r = m-1, n-1
# [0, 1, 6, 7, 9, 0, 0, 0] [3, 8, 9] 9 9
        for i in range(len(nums1)-1, -1, -1):
            if l >= 0 and r >= 0 and nums1[l] >= nums2[r]:
                nums1[i] = nums1[l]
                l -= 1
            elif r >= 0:
                nums1[i] = nums2[r] 
                r -= 1 
            else:
                break