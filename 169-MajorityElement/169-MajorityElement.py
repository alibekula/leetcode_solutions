# Last updated: 13.08.2025, 16:59:04
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res, count = 0, 0

        for num in nums:
            if count == 0:
                res = num
            
            if res != num:
                count -= 1
            else:
                count += 1
        
        return res