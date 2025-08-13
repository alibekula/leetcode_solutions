# Last updated: 13.08.2025, 16:58:42
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        if not nums:
            return 0


        l, r = 0, 0
        shortest = float('inf')
        curr = 0

        while r < len(nums):

            while r < len(nums) and curr < target:
                curr += nums[r]
                r += 1

            while l < r and curr >= target:
                shortest = min(shortest, r - l)
                curr -= nums[l]
                l += 1
                       
        return shortest if shortest != float('inf') else 0



        
        