# Last updated: 13.08.2025, 16:57:42
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2:
            return []
        
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        dct = {}
        ans = []

        for elem in nums1:
            if elem in dct:
                dct[elem] += 1
            else:
                dct[elem] = 1
        
        for item in nums2:
            if item in dct:
                if dct[item] > 0:
                    dct[item] -= 1
                    ans.append(item)
                if dct[item] == 0:
                    del dct[item]
        
        return ans
            

        