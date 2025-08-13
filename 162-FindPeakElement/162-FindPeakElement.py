# Last updated: 13.08.2025, 16:59:07
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        max_val = (float('-inf'), 0)

        while l < r:
            
            mid = (l+r)//2

            if nums[mid] < nums[mid+1]:
                l = mid + 1
            else:
                r = mid
        
        return l

        