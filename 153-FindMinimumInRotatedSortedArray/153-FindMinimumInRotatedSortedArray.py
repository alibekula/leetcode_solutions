# Last updated: 13.08.2025, 16:59:10
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1 
        while l < r:
            mid = (l+r)//2
            if nums[mid] > nums[r]:
                l = mid +1
            else:
                r = mid 
        return nums[l]
            