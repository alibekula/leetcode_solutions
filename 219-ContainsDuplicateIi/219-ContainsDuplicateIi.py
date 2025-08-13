# Last updated: 13.08.2025, 16:58:33
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dct = {}

        for idx, elem in enumerate(nums):

            if elem not in dct:
                dct[elem] = idx
            else:
                if idx - dct[elem] <= k:
                    return True
                else:
                    dct[elem] = idx
            
        return False
        