# Last updated: 30.09.2025, 09:27:20
from collections import deque
class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        
        if len(nums) < 1:
            return nums[0]

        queue = deque(nums[:])

        while len(queue) != 1:
            width = len(queue)

            for _ in range(width-1):
                num1 = queue.popleft()
                num2 = queue[0]
                val = (num1 + num2) % 10
                queue.append(val)

            queue.popleft()

        return queue.popleft()
