# Last updated: 13.08.2025, 17:01:00
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1

        while l <= r:

            mid = (l+r)//2

            if nums[mid] < target:
                l = mid+1
            else:
                r = mid - 1
        
        pos_l = l
        l, r = 0, len(nums)-1

        while l <= r:

            mid = (l+r) //2

            if nums[mid] > target:
                r = mid - 1
            else:
                l = mid+ 1
        
        pos_r = r
        
        if pos_l >= len(nums) or pos_r < 0 or nums[pos_l] != nums[pos_r]:
            return [-1, -1]
        else:
            return [pos_l, pos_r]


