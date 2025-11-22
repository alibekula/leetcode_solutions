# Last updated: 22.11.2025, 21:04:05
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        arr = sorted(nums)
        hashmap = {}

        rank = 0
        n = len(nums)

        for i in range(n):
            if arr[i] not in hashmap:
                hashmap[arr[i]] = rank
            rank += 1

        ans = []

        for num in nums:
            ans.append(hashmap[num])
        
        return ans
