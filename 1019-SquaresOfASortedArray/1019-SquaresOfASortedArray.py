# Last updated: 13.08.2025, 16:56:40
from collections import deque
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        lst = deque()

        l, r = 0, len(nums)-1

        while l <= r:
            if abs(nums[l]) >= abs(nums[r]):
                lst.appendleft(nums[l]**2)
                l += 1
            else:
                lst.appendleft(nums[r]**2)   
                r -= 1
        
        return list(lst)