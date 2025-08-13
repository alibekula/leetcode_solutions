# Last updated: 13.08.2025, 16:56:12
class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        l, r = 1,max(nums)
        min_val = 0

        while l <= r:
            mid = (l+r)//2
            count = 0

            idx = 0
            while idx < len(nums):
                if nums[idx] <= mid:
                    count += 1
                    idx += 2
                else:
                    idx += 1
            
            if count >= k:
                r = mid - 1
                min_val = mid
            else:
                l = mid + 1
        
        return min_val