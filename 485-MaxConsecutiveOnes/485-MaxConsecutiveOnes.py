# Last updated: 13.08.2025, 16:57:22
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        count = 0

        for num in nums:
            if num == 1:
                count += 1
            else:
                count = 0
            
            max_count = max(count, max_count)
        
        return max_count

        