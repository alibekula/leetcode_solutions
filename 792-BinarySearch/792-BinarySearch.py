# Last updated: 13.08.2025, 16:56:52
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) -1
        
        while l <= r:
            mid = (r-l)//2 + l
            if target < nums[mid]:
                r = mid - 1
            elif target > nums[mid]:
                l = mid + 1

            else:
                return mid
        return -1


