# Last updated: 13.08.2025, 16:56:03
class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:

        if len(nums) <= 1:
            return len(nums)

        l1, r1 = 0, 1
        l2, r2 = 0, 1
        longest1 = 1
        longest2 = 1
        # 1 2 4 0 1 2
        # 1 2 3 4
        # 1 4 3 3 2

        while r1 < len(nums) or r2 < len(nums):
            
            start1 = l1
            while r1 < len(nums) and nums[r1] > nums[l1]:
                longest1 = max(longest1, r1-start1+1)
                l1 += 1
                r1 += 1
            
            start2 = l2
            while r2 < len(nums) and nums[r2] < nums[l2]:
                longest2 = max(longest2, r2-start2+1)
                l2 += 1
                r2 += 1
            
            l1 = r1
            l2 = r2
            r1 += 1
            r2 += 1
            
        
        return max(longest1, longest2)

        