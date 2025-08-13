# Last updated: 13.08.2025, 16:58:16
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l, r = 0, 0
        queue =deque([])
        ans = []

        while r < len(nums):
            while queue and nums[r] >= nums[queue[-1]]:
                queue.pop()
            
            queue.append(r)

            if l-1 == queue[0]:
                queue.popleft()
            
            if r-l == k-1:
                r += 1
                l += 1
                ans.append(nums[queue[0]])
            else:
                r += 1
        
        return ans
