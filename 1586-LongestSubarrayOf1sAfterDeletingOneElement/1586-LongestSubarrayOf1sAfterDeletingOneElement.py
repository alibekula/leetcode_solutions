# Last updated: 13.08.2025, 16:56:27
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l, r= 0, 0
        longest = 0
        k = 1

        while r < len(nums):

            if nums[r] == 0:
                k -= 1

            if k < 0:
                while k < 0:
                    if nums[l] == 0:
                        k += 1
                    l += 1
            
            longest = max(longest, r-l)
            r += 1

        return longest



        