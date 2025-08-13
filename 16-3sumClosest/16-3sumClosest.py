# Last updated: 13.08.2025, 17:01:20
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closest = float('inf')
        nums.sort()

        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l, r = i + 1, len(nums) -1

            while l < r:

                total = nums[i] + nums[r] + nums[l]

                if target == total:
                    return total

                if abs(target - total) < abs(target - closest):

                    closest = total

                

                if total > target:
                    r -= 1
                
                else:
                    l += 1
    
        return closest

                    



