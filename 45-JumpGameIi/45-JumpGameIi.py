# Last updated: 13.08.2025, 17:00:49
class Solution:
    def jump(self, nums: List[int]) -> int:
        
        n = len(nums)-1
        max_reach = 0
        curr = 0
        jumps = 0
        
        for i in range(n):
            max_reach = max(max_reach, nums[i] + i)

            if i == curr:
                jumps += 1
                curr = max_reach

                if curr >= n:
                    return jumps

        return jumps


        