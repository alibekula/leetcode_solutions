# Last updated: 10.10.2025, 22:20:05
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        n = len(nums)
        l, r = 0, 0
        zero = False
        length = 0
        # 1 0 1 1 1 0 0 1
        while r < n:

            while r < n and (nums[r] != 0 or not zero):
                if nums[r] == 0:
                    zero = True
                length = max(length, r-l)
                r += 1

            
            while l < r and zero:
                if nums[l] == 0:
                    zero = False
                l += 1

        return length

