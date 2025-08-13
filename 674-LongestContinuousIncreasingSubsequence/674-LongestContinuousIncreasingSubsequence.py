# Last updated: 13.08.2025, 16:57:04
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        longest = 0
        l, r = 0, 0

        while r < len(nums):
            l = r

            while r + 1 < len(nums) and nums[r] < nums[r+1]:
                r += 1
            
            longest = max(longest, r-l + 1)
            r += 1
        
        return longest

# [1]
# [1, 2]
