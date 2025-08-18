# Last updated: 19.08.2025, 03:37:25
import heapq

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        
        if total % 2 != 0:
            return False
        
        target = total//2
        dp = {0}

        for num in nums:
            items = set()

            for curr in dp:
                items.add(num + curr)

                if num + curr == target:
                    return True
                
            dp.update(items)

        return target in dp

