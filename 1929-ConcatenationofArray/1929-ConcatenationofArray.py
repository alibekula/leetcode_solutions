# Last updated: 22.11.2025, 20:46:20
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        consec = 0
        nums.append(0)
        for num in nums:
            if num == 0:
                max_count = max(max_count, consec)
                consec = 0
            else:
                consec += 1
        
        return max_count
        