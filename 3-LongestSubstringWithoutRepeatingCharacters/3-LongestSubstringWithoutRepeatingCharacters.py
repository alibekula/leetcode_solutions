# Last updated: 27.09.2025, 06:45:45
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        total = 0
        curr = 0
        prefix = {0:1}

        for num in nums:
            curr += num

            if curr - k in prefix:
                total += prefix[curr-k]

            prefix[curr] = prefix.get(curr, 0) + 1

        return total