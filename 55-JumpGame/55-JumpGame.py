# Last updated: 13.08.2025, 17:00:39
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        pos = 0
        max_pos = len(nums)
        max_reachable = 0
        for i in range(max_pos):
            if i > max_reachable:
                return False
            max_reachable = max(max_reachable, i + nums[i])
            if max_reachable >= max_pos-1:
                return True
        return False
                
        