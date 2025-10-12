# Last updated: 12.10.2025, 15:43:07
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        nums = [i if i != 0 else -1 for i in nums]
        n = len(nums)
        prefix = {0:-1}
        curr = 0
        ans = 0

        for idx, num in enumerate(nums):
            curr += num

            if curr in prefix:
                ans = max(ans, idx - prefix[curr])
            else:
                prefix[curr] = idx
        
        return ans