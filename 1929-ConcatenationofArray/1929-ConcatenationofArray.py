# Last updated: 22.11.2025, 20:55:35
from collections import Counter
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        counter = {key: 0 for key in range(1, len(nums)+1)}
        ans = [-1, -1]

        for num in nums:
            counter[num] += 1

        for key, value in counter.items():
            if value == 2:
                ans[0] = key
            elif value == 0:
                ans[1] = key

        return ans