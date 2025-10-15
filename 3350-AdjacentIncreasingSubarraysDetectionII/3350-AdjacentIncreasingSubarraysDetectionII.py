# Last updated: 15.10.2025, 20:14:16
class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        
        n = len(nums)
        decr = [0] * n

        for i in range(n-2, -1, -1):
            j= i + 1

            if nums[i] < nums[j]:
                decr[i] = decr[j] + 1
        
        max_k = 1

        for i in range(n):

            k = decr[i] + 1

            if k > 1:
                max_k = max(max_k, k // 2)
            if i + k < n and decr[i] <= decr[i +k]:
                max_k = max(max_k, k) 
        
        return max_k