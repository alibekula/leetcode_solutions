# Last updated: 13.08.2025, 16:57:16
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dct = {0:1}
        curr = 0
        r = 0
        total = 0

        while r < len(nums):
            curr += nums[r]

            if k - curr in dct: 
                total += dct[k-curr]
            
            if -curr not in dct:
                dct[-curr] = 0
            
            dct[-curr] += 1
            r += 1
        
        return total