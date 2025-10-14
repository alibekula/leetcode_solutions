# Last updated: 14.10.2025, 14:18:18
class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        
        n = len(nums)
        decr = [0] * n

        if k ==1:
            return True

        for j in range(n-1, 0, -1):
            i = j - 1

            if nums[j] > nums[i]:
                decr[i] = decr[j] + 1
        
        for i in range(n):
            if decr[i] >= k-1:
                if (i + k < n and decr[i+k] >= k-1):
                    return True
        
        return False


