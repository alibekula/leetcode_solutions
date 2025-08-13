# Last updated: 13.08.2025, 16:56:11
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()

        high_count = 0
        low_count = 0
        l, r = 0, len(nums)-1

        while l < r:
            if nums[l] + nums[r] <= upper:
                high_count += r - l
                l += 1
            else:
                r -= 1
        
        l, r = 0, len(nums)-1

        while l < r:
            if nums[l] + nums[r] <= lower - 1:
                low_count += r - l
                l += 1
            else:
                r -= 1

        return high_count - low_count