# Last updated: 25.09.2025, 21:57:46
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        longest = 0

        l, r = 0, 0 
        k = 1

        while r < len(nums):
            
            if nums[r] == 0:
                k -= 1

            while k < 0:
                if nums[l] == 0:
                    k += 1
                
                l += 1
            
            longest=max(longest, r-l+k)
            r += 1
        
        return longest if longest != len(nums) else longest -1



