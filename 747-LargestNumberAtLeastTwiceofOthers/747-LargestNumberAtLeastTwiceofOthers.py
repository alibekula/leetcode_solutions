# Last updated: 12.10.2025, 16:15:32
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        
        largest, index = max([(val, idx) for idx,val in enumerate(nums)])
        half = largest // 2

        for idx, num in enumerate(nums):
            if idx != index and num > half:
                return -1
        
        return index