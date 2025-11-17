# Last updated: 17.11.2025, 19:23:32
class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        
        prev, curr = None, None

        for i in range(len(nums)):
            
            if nums[i] == 1:

                if prev is None:
                    prev = i
                    continue

                curr = i
                
                if curr - prev - 1 < k:
                    return False

                prev = curr
        return True