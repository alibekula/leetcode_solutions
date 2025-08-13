# Last updated: 13.08.2025, 16:56:38
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zeros_count = 0
        l, r = 0, 0
        longest = 0

        while r < len(nums):

            if nums[r] == 0:
                zeros_count += 1
            
            while l <= r and zeros_count > k:
                if nums[l] == 0:
                    zeros_count -= 1
                l += 1
            
            longest = max(longest, r-l+1)

            r += 1
        
        return longest

        